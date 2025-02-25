use Lab13
go

-- �������� ������� Fact_Orders
CREATE TABLE Fact_Orders (
    factOrderId INT IDENTITY(1,1) PRIMARY KEY,  -- ���������� ������������� ������ � Fact_Orders
    orderId INT NOT NULL,       -- �����
    userId INT NOT NULL,        -- ������ (����������� �����)
    driverId INT NOT NULL,      -- ��������
    cargoId INT NOT NULL,       -- ����
    routeId INT NOT NULL,       -- �������
    paymentId INT NOT NULL,     -- ������
    price DECIMAL(10,2) NOT NULL, -- ��������� ������
    status VARCHAR(50) NOT NULL, -- ������ ������ (��������, "��������", "�������")
    orderDate DATETIME NOT NULL, -- ���� ���������� ������
    weight DECIMAL(10,2) NOT NULL, -- ��� �����
    volume DECIMAL(10,2) NOT NULL, -- ����� �����
    rating DECIMAL(3,2),          -- ������� �������� (���� ����)

    -- ������� �����
    FOREIGN KEY (orderId) REFERENCES Orders(orderId),
    FOREIGN KEY (userId) REFERENCES Users(userId),
    FOREIGN KEY (driverId) REFERENCES Users(userId),
    FOREIGN KEY (cargoId) REFERENCES Cargo(cargoId),
    FOREIGN KEY (routeId) REFERENCES Routes(routeId),
    FOREIGN KEY (paymentId) REFERENCES Payments(paymentId)
);

drop table Fact_Orders

INSERT INTO Fact_Orders (orderId, userId, driverId, cargoId, routeId, paymentId, price, status, orderDate, weight, volume, rating)
SELECT 
    o.orderId, 
    c.clientId AS userId, 
    v.driverId, 
    o.orderCargo AS cargoId, 
    o.orderRoute AS routeId, 
    p.paymentId, 
    o.price, 
    o.status, 
    o.createdAt AS orderDate, 
    c.weight, 
    c.volume, 
    r.rating
FROM Orders o
JOIN Cargo c ON o.orderCargo = c.cargoId
JOIN Vehicles v ON o.orderVehicle = v.vehicleId
JOIN Payments p ON o.orderId = p.paymentOrder
LEFT JOIN Reviews r ON o.orderId = r.reviewOrder;  -- ���������� LEFT JOIN, �.�. �� ��� ������ ����� ������

select * from Fact_Orders



ALTER TABLE Fact_Orders 
ALTER COLUMN price DECIMAL(12,2);  -- ���������� �����������
ALTER TABLE Fact_Orders 
ALTER COLUMN weight DECIMAL(12,2);
ALTER TABLE Fact_Orders 
ALTER COLUMN volume DECIMAL(12,2);
ALTER TABLE Fact_Orders 
ALTER COLUMN rating DECIMAL(4,2);  -- ����� ������� 10 ����� ����


USE [master]
GO
CREATE LOGIN [NT Service\MSSQLServerOLAPService] FROM WINDOWS
GO
ALTER SERVER ROLE sysadmin ADD MEMBER [adm]
GO