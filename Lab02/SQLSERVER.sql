
use mshoad

select * from Roles;
insert into Roles values 
('admin'),
('driver'),
('shipper');

select * from Users;
insert into Users (firstName,lastName,fatherName,email,password,phone,role,INN,userType,verified)
values
('Cristiano','Ronaldo',null,'cr7.exmaple@.com','cr7isgood','80291313441',2,'HFEHA233KE','Юрид. лицо',1 ),
('Vladislav','Lemiashusky','Olegovich','vlad.lemeshok@gmail.com','qwerty12345','80290384288',3,'FFEJ324BBJE','Юрид. лицо',1 );


select * from Cargo;
insert into Cargo
values
('Big box of apples',50,150,'BOX','Minsk','Madrid',1);

select * from Vehicles;
insert into Vehicles 
(driverId,model,type,capacity,licencePlate,brand)
values
(2,'Track','Big Sized', 3000, 8029,'Mercedes-Benz');

select * from Routes;
insert into Routes
values
(1500,GETDATE() , GETDATE());

select * from Orders;
insert into Orders
(orderCargo,orderVehicle,price,status,orderRoute)
values
(1,1,2500,'pending',1);

select* from Payments;
insert into Payments
(paymentOrder,amount,paymentMethod,paymentStatus)
values
(1,2500,'credit_card','pending');

select * from Reviews;
insert into Reviews
(reviewOrder,reviewerId,reviewComment,reviewedVehicle,rating)
values
(1,1,'Made fast and good',1,9);








--- VehicleOrderCargoRouteUser

create view VehicleOrderCargoRouteUser as 
select O.orderId , O.price, O.status , C.cargoId , 
C.description , C.weight , C.volume, C.bodyType,
V.vehicleId , V.driverId, V.model , V.licencePlate, R.routeId ,
R.distance , R.loadingDate , R.uploadingDate,
U.userId , U.firstName , U.lastName , U.phone , U.email
from Orders O
inner join Cargo C on C.cargoId = O.orderCargo
inner join Vehicles V on V.vehicleId = O.orderVehicle
inner join Routes R on R.routeId = O.orderRoute
inner join Users U on U.userId = C.clientId;


select * from VehicleOrderCargoRouteUser;




--- ReviewVehicleOrderUser


create view ReviewVehicleOrderUser as 
select O.orderId , O.price, O.status ,
V.vehicleId , V.driverId, V.model , V.licencePlate,
U.userId , U.firstName , U.lastName , U.phone , U.email,
R.rating, R.reviewerId , R.reviewComment , R.reviewOrder , R.reviewedVehicle
from Orders O
inner join Vehicles V on V.vehicleId = O.orderVehicle
inner join Reviews R on R.reviewOrder = O.orderId
inner join Users U on U.userId = R.reviewerId;

select * from ReviewVehicleOrderUser;


--- UsersPaymentsOrdersVehicles


create view UsersPaymentsOrdersVehicles as 
select O.orderId , O.price, O.status ,
U.userId , U.firstName , U.lastName , U.phone , U.email,
P.amount , P.paymentDate , P.paymentMethod , P.paymentOrder ,P.paymentStatus,
V.driverId , V.licencePlate, V.brand
from Orders O
inner join Cargo C on C.cargoId = O.orderCargo 
inner join Payments P on P.paymentOrder = O.orderId 
inner join Users U on U.userId = C.clientId
inner join Vehicles V on V.vehicleId = O.orderVehicle;

select * from ReviewVehicleOrderUser;


drop view VehicleOrderCargoRouteUser;
drop view ReviewVehicleOrderUser;
drop view UsersPaymentsOrdersVehicles;


--- Procedure Insert Users

create procedure InsertUser
	@fName varchar(255),
	@lName varchar(255),
	@faName varchar(255),
	@em varchar(255),
	@pass varchar(255),
	@tel varchar(25),
	@rId int,
	@inn varchar(50),
	@uType varchar(150),
	@vf BIT
as
insert into Users (firstName,lastName,fatherName,email,password,phone,role,INN,userType,verified)
values
(@fName,@lName,@faName,@em,@pass,@tel,@rId,@inn,@uType,@vf )
;


exec InsertUser 'Travis', 'Scott' , null,
'exmaple@gmail.com','qwertobobob','80299876655',2,'FEFEIW123WIE','ИП',1;



--- Индексы

create unique index IX_User_Email on Users(email)
INCLUDE(firstName,lastName,fatherName,password,phone,INN,userType,
creationDate,verified);
create index IX_Cargo_Desc on Cargo(description);
create index IX_Vehicle_Plate on Vehicles(licencePlate);
create index IX_Order_Status on Orders(status)
INCLUDE(price,createdAt);
create index IX_Review_Rate on Reviews(rating);

drop index IX_User_email on Users;
drop index IX_Cargo_Desc on Cargo;
drop index IX_Vehicle_Plate on Vehicles;
drop index IX_Order_Status  on Orders;
drop index IX_Review_Rate  on Reviews;


--- Триггер:

create trigger Users_INSERTED 
on Users
AFTER INSERT
as
select * from inserted;

create trigger Cargo_UPDATED
on Cargo
AFTER UPDATE
as
select cargoId , ' Обновлен груз: ' + bodyType + ' грузоотправителя: ' 
+ CAST(clientId as varchar) from inserted;

create trigger Order_DELETED
on Orders
AFTER DELETE
as
select orderId, 'Удален заказ товара: ' +  CAST(orderCargo as varchar) + ' в статусе ' + status  
from deleted;


drop trigger Users_INSERTED;
drop trigger Cargo_UPDATED;
drop trigger Order_DELETED;


-- sequence next value for ...

CREATE SEQUENCE table_identifier
    START WITH 1
    INCREMENT BY 1;




	--- function


CREATE FUNCTION dbo.AVG_RATE
(
    @REVIEW INT
)
RETURNS DECIMAL(18, 2)
AS
BEGIN
    DECLARE @RATE_CURS CURSOR;
    DECLARE @RATE_VALUE INT;
    DECLARE @CNT INT = 0;
    DECLARE @SUM_RATE INT = 0;
    DECLARE @AVG_RATE DECIMAL(18, 2) = 0;

    SET @RATE_CURS = CURSOR FOR 
    SELECT rating 
    FROM Reviews 
    WHERE reviewId = @REVIEW;

    OPEN @RATE_CURS;

    FETCH NEXT FROM @RATE_CURS INTO @RATE_VALUE;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @SUM_RATE = @SUM_RATE + @RATE_VALUE;
        SET @CNT = @CNT + 1;

        FETCH NEXT FROM @RATE_CURS INTO @RATE_VALUE;
    END

    CLOSE @RATE_CURS;
    DEALLOCATE @RATE_CURS;
    IF @CNT > 0
    BEGIN
        SET @AVG_RATE = @SUM_RATE / @CNT;
    END

    RETURN @AVG_RATE;
END;
GO

drop function AVG_RATE;

SELECT dbo.AVG_RATE(1) AS AverageRating;