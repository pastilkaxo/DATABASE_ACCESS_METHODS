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
userType varchar(150) not null CHECK(userType = '��' OR userType = '����. ����' OR userType = '���. ����'),
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




-- ������� �������������
INSERT INTO Users (firstName, lastName, fatherName, email, password, phone, role, INN, userType, verified) VALUES
('����', '������', '��������', 'ivan@example.com', 'password1', '1234567890', 1, '123456789012', '��', 1),
('����', '������', '��������', 'petr@example.com', 'password2', '0987654321', 2, '987654321012', '����. ����', 0),
('�����', '�������', '���������', 'sidor@example.com', 'password3', '5555555555', 3, '111111111111', '���. ����', 0);

-- ������� ������
INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId) VALUES
('���� 1', 1000.00, 1.00, '�����', '����� 1', '����� 2', 1),
('���� 2', 2000.00, 2.00, '������', '����� 3', '����� 4', 2),
('���� 3', 1500.00, 1.50, '���������', '����� 5', '����� 6', 1);

-- ������� ������������ �������
INSERT INTO Vehicles (driverId, model, type, capacity, licencePlate, brand) VALUES
(2, '������ 1', '��������', 5000, 23, '����� 1'),
(3, '������ 2', '��������', 1500, 24, '����� 2'),
(4, '������ 3', '��������', 7000, 123, '����� 3');

-- ������� ���������
INSERT INTO Routes (distance, loadingDate, uploadingDate) VALUES
(100, '2025-02-25 10:00:00', '2025-02-25 12:00:00'),
(200, '2025-02-26 10:00:00', '2025-02-26 12:00:00'),
(150, '2025-02-27 10:00:00', '2025-02-27 12:00:00');

-- ������� �������
INSERT INTO Orders (orderCargo, orderVehicle, price, status, orderRoute) VALUES
(1, 5, 5000.00, 'pending', 1),
(2, 6, 10000.00, 'completed',1),
(3, 7, 7500.00, 'pending',1);

-- ������� ��������
INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus) VALUES
(10, 5000.00, 'credit_card', 'completed'),
(11, 10000.00, 'bank_transfer', 'pending'),
(12, 7500.00, 'credit_card', 'completed');

-- ������� �������
INSERT INTO Reviews (reviewOrder, reviewerId, reviewComment, reviewedVehicle, rating) VALUES
(10, 3, '�������� ����!', 5, 10),
(11, 4, '�������� ������ ��� �������.', 6, 9),
(12, 5, '�� �����������.', 7, 8);
