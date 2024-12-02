create database mshoad;


use mshoad;
go
create table Roles(
roleId int identity(1,1) primary key,
roleName varchar(255) not null check (roleName = 'admin' or roleName = 'driver' or roleName = 'shipper')
);
create table Users(
userId INT identity(1,1) primary key,
firstName varchar(255) not null,
lastName varchar(255) not null,
fatherName varchar(255) ,
email varchar(255) not null unique,
password varchar(255) not null,
phone varchar(25) not null,
role int not null,
INN varchar(50) not null,
userType varchar(150) not null CHECK(userType = 'ИП' OR userType = 'Юрид. лицо' OR userType = 'Физ. лицо'),
creationDate datetime not null default GETDATE(),
verified bit default 0 not null,
foreign key (role) references Roles(roleId)
);
create table Cargo(
cargoId int identity(1,1) primary key,
description varchar(255) not null,
weight decimal(10,2) not null,
volume decimal(10,2) not null ,
bodyType varchar(100) not null,
loadingAddress varchar(100) not null,
uploadingAddress varchar(100) not null,
clientId int ,
foreign key (clientId) references Users(userId)
);
create table Vehicles (
vehicleId int identity(1,1) primary key,
driverId int not null,
model varchar(100) not null,
type varchar(50) not null,
capacity int not null,
licencePlate int not null,
brand varchar(100) not null,
addDate datetime default GETDATE(),
foreign key(driverId) references Users(userId)
);
create table Routes(
routeId int identity(1,1) primary key,
distance int not null,
loadingDate datetime not null,
uploadingDate datetime not null,
);
create table Orders (
orderId int identity(1,1) primary key,
orderCargo int not null,
orderVehicle int not null,
price decimal(10,2) not null,
status varchar(150) not null default 'pending',
createdAt datetime default GETDATE(),
orderRoute int not null,
foreign key (orderRoute) references Routes(routeId),
foreign key (orderCargo) references Cargo(cargoId),
foreign key (orderVehicle) references Vehicles(vehicleId)
);
create table Payments (
paymentId int identity(1,1) primary key,
paymentOrder int not null,
amount decimal(10,2) not null,
paymentMethod varchar(100) not null default 'credit_card',
paymentStatus varchar(150) not null default 'pending',
paymentDate datetime default GETDATE(),
foreign key (paymentOrder) references Orders(orderId)
);
create table Reviews (
reviewId int identity(1,1) primary key,
reviewOrder int not null,
reviewerId int not null,
reviewComment varchar(255) not null,
reviewedVehicle int not null,
rating int not null check ( rating >=1 AND rating <= 10),
foreign key (reviewOrder) references Orders(orderId),
foreign key (reviewerId) references Users(userId),
foreign key (reviewedVehicle) references Vehicles(vehicleId)
);


drop table Routes;
drop table Reviews;
drop table Payments;
drop table Orders;
drop table Cargo;
drop table Vehicles;
drop table Users;
drop table Roles;
