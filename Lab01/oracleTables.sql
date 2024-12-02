ALTER SESSION SET "_oracle_script" = false; 

create user MSHOAD_DEV identified by 12345;
grant 
create session,
connect,
CREATE TABLE,
CREATE VIEW,
CREATE PROCEDURE,
CREATE ANY INDEX,
CREATE USER,
DROP  USER,
CREATE SEQUENCE,
CREATE TRIGGER,
CREATE ROLE,
CREATE TYPE,
CREATE ANY DIRECTORY
TO
MSHOAD_DEV
;

alter user MSHOAD_DEV quota unlimited on USERS;

grant execute on sys.dbms_crypto to MSHOAD_DEV;

create table Roles(
roleId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
roleName varchar(255) not null check (roleName IN ('admin', 'driver', 'shipper'))
);
create table Users(
userId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
firstName varchar(255) not null,
lastName varchar(255) not null,
fatherName varchar(255) ,
email varchar(255) not null unique,
password varchar(255) not null,
phone varchar(25) not null,
role number not null,
INN varchar(50) not null,
userType varchar(150) not null CHECK(userType IN ('ИП', 'Юрид. лицо', 'Физ. лицо')),
creationDate DATE DEFAULT SYSDATE not null ,
verified NUMBER(1) not null CHECK (verified IN (0, 1)),
CONSTRAINT FK_USERS_ROLES foreign key (role) references Roles(roleId)
);
create table Cargo(
cargoId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
description varchar(255) not null,
weight decimal(10,2) not null,
volume decimal(10,2) not null ,
bodyType varchar(100) not null,
loadingAddress varchar(100) not null,
uploadingAddress varchar(100) not null,
clientId number ,
CONSTRAINT FK_CARGO_USERS foreign key (clientId) references Users(userId)
);
create table Vehicles (
vehicleId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
driverId number not null,
model varchar(100) not null,
type varchar(50) not null,
capacity number not null,
licencePlate number not null UNIQUE,
brand varchar(100) not null,
addDate date DEFAULT SYSDATE,
CONSTRAINT FK_VEHICLES_USERS foreign key(driverId) references Users(userId)
);
create table Routes(
routeId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
distance number not null,
loadingDate DATE not null,
uploadingDate DATE not null
);
create table Orders (
orderId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
orderCargo number not null,
orderVehicle number not null,
price decimal(10,2) not null,
status varchar(150)  default 'pending' not null ,
createdAt DATE default SYSDATE,
orderRoute number not null,
CONSTRAINT FK_ORDERS_ROUTES foreign key (orderRoute) references Routes(routeId),
CONSTRAINT FK_ORDERS_CARGO foreign key (orderCargo) references Cargo(cargoId),
CONSTRAINT FK_ORDERS_VEHICLES foreign key (orderVehicle) references Vehicles(vehicleId)
);
create table Payments (
paymentId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
paymentOrder number not null,
amount decimal(10,2) not null,
paymentMethod varchar(100) default 'credit_card' not null ,
paymentStatus varchar(150) default 'pending' not null ,
paymentDate DATE DEFAULT SYSDATE not null ,
CONSTRAINT FK_PAYMENTS_ORDERS foreign key (paymentOrder) references Orders(orderId)
);
create table Reviews (
reviewId number GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) primary key,
reviewOrder number not null,
reviewerId number not null,
reviewComment varchar(255) not null,
reviewedVehicle number not null,
rating number not null check ( rating >=1 AND rating <= 10),
CONSTRAINT FK_REVIEWS_ORDERS foreign key (reviewOrder) references Orders(orderId),
CONSTRAINT FK_REVIEWS_USERS foreign key (reviewerId) references Users(userId),
CONSTRAINT FK_REVIEWS_VEHICLES foreign key (reviewedVehicle) references Vehicles(vehicleId)
);

drop table Reviews;
drop table Payments;
drop table Orders;
drop table Routes;
drop table Cargo;
drop table Vehicles;
drop table Users;
drop table Roles;
