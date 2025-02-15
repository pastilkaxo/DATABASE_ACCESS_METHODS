-- Insert
INSERT INTO Roles (roleName) VALUES ('admin');
INSERT INTO Roles (roleName) VALUES ('driver');
INSERT INTO Roles (roleName) VALUES ('shipper');

INSERT INTO Users (firstName, lastName, fatherName, email, password, phone, role, INN, userType, verified)
VALUES ('Cristiano', 'Ronaldo', NULL, 'cr7.exmaple@.com', 'cr7isgood', '80291313441', 2, 'HFEHA233KE', 'Юрид. лицо', 1);

INSERT INTO Users (firstName, lastName, fatherName, email, password, phone, role, INN, userType, verified)
VALUES ('Vladislav', 'Lemiashusky', 'Olegovich', 'vlad.lemeshok@gmail.com', 'qwerty12345', '80290384288', 3, 'FFEJ324BBJE', 'Юрид. лицо', 1);

INSERT INTO Users (firstName, lastName, email, password, phone, role, INN, userType, verified)
VALUES ('Lionel', 'Messi', 'messi@example.com', 'messiisgreat', '80291313442', 2, 'HFEHA233KF', 'Юрид. лицо', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Big box of apples', 50, 150, 'BOX', 'Minsk', 'Madrid', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Small box of oranges', 20, 80, 'BOX', 'Minsk', 'Barcelona', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Medium box of bananas', 30, 100, 'BOX', 'Minsk', 'Berlin', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Box of apples', 35, 105, 'BOX', 'Minsk', 'Moscow', 3);


INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Box of grapes', 40, 120, 'BOX', 'Minsk', 'Paris', 1); -- CargoId = 5

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Box of pears', 45, 130, 'BOX', 'Minsk', 'Rome', 1); -- CargoId = 6


INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Box of milk', 45, 130, 'BOX', 'Minsk', 'Washington', 1); -- CargoId = 6



INSERT INTO Vehicles (driverId, model, type, capacity, licencePlate, brand)
VALUES (2, 'Track', 'Big', 3000, '8029', 'Mercedes-Benz');

INSERT INTO Vehicles (driverId, model, type, capacity, licencePlate, brand)
VALUES (3, 'Van', 'Medium', 1500, '8030', 'Ford');

INSERT INTO Routes (distance, loadingDate, uploadingDate)
VALUES (1500, SYSDATE, SYSDATE);

INSERT INTO Routes (distance, loadingDate, uploadingDate)
VALUES (1200, SYSDATE, SYSDATE);

INSERT INTO Routes (distance, loadingDate, uploadingDate)
VALUES (12200, SYSDATE, SYSDATE);

INSERT INTO Routes (distance, loadingDate, uploadingDate)
VALUES (100, SYSDATE, SYSDATE);
--------------------------------------



-- Заказы с пересечением (Один и тот же заказ встречается у разных грузов)
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (5, 1, 9000.00, 'completed', TO_DATE('2023-04-10', 'YYYY-MM-DD'), 1); -- OrderId = 10

INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (6, 1, 9000.00, 'completed', TO_DATE('2023-04-10', 'YYYY-MM-DD'), 1); -- OrderId = 11

-- Дублируем заказ в другой груз (Пересечение)
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (5, 1, 7500.00, 'completed', TO_DATE('2023-04-15', 'YYYY-MM-DD'), 2); -- OrderId = 12

INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (6, 1, 7500.00, 'completed', TO_DATE('2023-04-15', 'YYYY-MM-DD'), 2); -- OrderId = 12 (Пересечение!)


-- Данные для типа транспорта "Big"
-- Рост -> Падение -> Рост
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (1, 1, 5000.00, 'completed', TO_DATE('2023-01-10', 'YYYY-MM-DD'), 1); -- Январь
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (2, 1, 5000.00, 'completed', TO_DATE('2023-01-15', 'YYYY-MM-DD'), 1); -- Январь


INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (3, 1, 3000.00, 'completed', TO_DATE('2023-02-10', 'YYYY-MM-DD'), 2); -- Февраль


INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (1, 1, 7000.00, 'completed', TO_DATE('2023-03-10', 'YYYY-MM-DD'), 3); -- Март
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (2, 1, 8000.00, 'completed', TO_DATE('2023-03-15', 'YYYY-MM-DD'), 3); -- Март
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (3, 1, 8000.00, 'completed', TO_DATE('2023-03-15', 'YYYY-MM-DD'), 3); -- Март
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (4, 1, 8000.00, 'completed', TO_DATE('2023-03-15', 'YYYY-MM-DD'), 3); -- Март

-- Данные для типа транспорта "Medium"
-- Рост -> Падение -> Рост
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (1, 2, 4000.00, 'completed', TO_DATE('2023-01-10', 'YYYY-MM-DD'), 4); -- Январь
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (2, 2, 3000.00, 'completed', TO_DATE('2023-01-15', 'YYYY-MM-DD'), 4); -- Январь
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (3, 2, 3000.00, 'completed', TO_DATE('2023-01-15', 'YYYY-MM-DD'), 4); -- Январь

INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (2, 2, 2000.00, 'completed', TO_DATE('2023-02-10', 'YYYY-MM-DD'), 1); -- Февраль

INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (1, 2, 6000.00, 'completed', TO_DATE('2023-03-10', 'YYYY-MM-DD'), 2); -- Март
INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (2, 2, 7000.00, 'completed', TO_DATE('2023-03-15', 'YYYY-MM-DD'), 2); -- Март


INSERT INTO Orders (orderCargo, orderVehicle, price, status, createdAt, orderRoute)
VALUES (2, 3, 7000.00, 'completed', TO_DATE('2023-03-15', 'YYYY-MM-DD'), 2); -- Март




--------------------------------------


INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus,paymentDate)
VALUES (1, 2500, 'credit_card', 'pending', TO_DATE('2024-03-10', 'YYYY-MM-DD'));

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 5000, 'paypal', 'completed', TO_DATE('2024-04-25', 'YYYY-MM-DD'));

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 1500, 'credit_card', 'completed', TO_DATE('2024-05-15', 'YYYY-MM-DD'));

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 2000, 'bank_transfer', 'completed', TO_DATE('2024-06-18', 'YYYY-MM-DD'));


INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 2300, 'bank_transfer', 'completed', TO_DATE('2024-09-03', 'YYYY-MM-DD'));

INSERT INTO Reviews (reviewOrder, reviewerId, reviewComment, reviewedVehicle, rating)
VALUES (1, 1, 'Made fast and good', 1, 9);


-- Views

CREATE VIEW VehicleOrderCargoRouteUser AS 
SELECT O.orderId, O.price, O.status, C.cargoId, C.description, C.weight, C.volume, C.bodyType,
       V.vehicleId, V.driverId, V.model, V.licencePlate, R.routeId, R.distance, R.loadingDate, R.uploadingDate,
       U.userId, U.firstName, U.lastName, U.phone, U.email
FROM Orders O
INNER JOIN Cargo C ON C.cargoId = O.orderCargo
INNER JOIN Vehicles V ON V.vehicleId = O.orderVehicle
INNER JOIN Routes R ON R.routeId = O.orderRoute
INNER JOIN Users U ON U.userId = C.clientId;

select * from VehicleOrderCargoRouteUser;

CREATE VIEW ReviewVehicleOrderUser AS 
SELECT O.orderId, O.price, O.status, V.vehicleId, V.driverId, V.model, V.licencePlate,
       U.userId, U.firstName, U.lastName, U.phone, U.email, R.rating, R.reviewerId, R.reviewComment, R.reviewOrder, R.reviewedVehicle
FROM Orders O
INNER JOIN Vehicles V ON V.vehicleId = O.orderVehicle
INNER JOIN Reviews R ON R.reviewOrder = O.orderId
INNER JOIN Users U ON U.userId = R.reviewerId;

select * from ReviewVehicleOrderUser;

CREATE VIEW UsersPaymentsOrdersVehicles AS 
SELECT O.orderId, O.price, O.status, U.userId, U.firstName, U.lastName, U.phone, U.email,
       P.amount, P.paymentDate, P.paymentMethod, P.paymentOrder, P.paymentStatus, V.driverId, V.licencePlate, V.brand
FROM Orders O
INNER JOIN Cargo C ON C.cargoId = O.orderCargo
INNER JOIN Payments P ON P.paymentOrder = O.orderId
INNER JOIN Users U ON U.userId = C.clientId
INNER JOIN Vehicles V ON V.vehicleId = O.orderVehicle;

select * from UsersPaymentsOrdersVehicles;


--- Procedure

CREATE OR REPLACE PROCEDURE InsertUser(
    fName IN VARCHAR2,
    lName IN VARCHAR2,
    faName IN VARCHAR2,
    em IN VARCHAR2,
    pass IN VARCHAR2,
    tel IN VARCHAR2,
    rId IN NUMBER,
    inn IN VARCHAR2,
    uType IN VARCHAR2,
    vf IN NUMBER
) AS
BEGIN
    INSERT INTO Users (firstName, lastName, fatherName, email, password, phone, role, INN, userType, verified)
    VALUES (fName, lName, faName, em, pass, tel, rId, inn, uType, vf);
END;


begin
 InsertUser('Travis', 'Scott' , null,
'exmaple@gmail.com','qwertobobob','80299876655',2,'FEFEIW123WIE','ИП',1);
end;

--- indexes

CREATE UNIQUE INDEX IX_User_Email ON Users(email);
CREATE INDEX IX_Cargo_Desc ON Cargo(description);
CREATE INDEX IX_Vehicle_Plate ON Vehicles(licencePlate);
CREATE INDEX IX_Order_Status ON Orders(status);
CREATE INDEX IX_Review_Rate ON Reviews(rating);

DROP INDEX IX_User_Email;
DROP INDEX IX_Cargo_Desc;
DROP INDEX IX_Vehicle_Plate;
DROP INDEX IX_Order_Status;
DROP INDEX IX_Review_Rate;


-- triggers

CREATE OR REPLACE TRIGGER Users_INSERTED 
AFTER INSERT ON Users
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('New user added: ' || :NEW.email);
END;

CREATE OR REPLACE TRIGGER Cargo_UPDATED
AFTER UPDATE ON Cargo
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('Cargo updated: ' || :NEW.bodyType || ' for client: ' || :NEW.clientId);
END;

CREATE OR REPLACE TRIGGER Order_DELETED
AFTER DELETE ON Orders
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('Order deleted: ' || :OLD.orderCargo || ' with status: ' || :OLD.status);
END;


-- Sequence:

create sequence table_identifier
minvalue 1
maxvalue 9999999999999
start with 1
increment by 1
cache 20
nocycle;


--- function


CREATE OR REPLACE FUNCTION HASH_PASS
    (PASSWORD IN NVARCHAR2)
    RETURN VARCHAR2
IS
BEGIN
    IF PASSWORD IS NULL OR LENGTH(PASSWORD) > 20  THEN 
        RETURN 'FALSE'; 
    ELSE
        RETURN DBMS_CRYPTO.HASH(UTL_I18N.STRING_TO_RAW(PASSWORD,'AL32UTF8'),DBMS_CRYPTO.HASH_SH256);    
    END IF;
EXCEPTION
        WHEN NO_DATA_FOUND THEN
        RETURN 'FALSE'; 
        WHEN TOO_MANY_ROWS THEN
        RETURN 'FALSE';
        WHEN OTHERS 
        THEN RETURN 'FALSE';
END;
