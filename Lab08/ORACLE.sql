--1.	Подключиться к серверу Oracle.
--2.	Создать объектные типы данных по своему варианту (Услуги(Машины) и заказы), реализовав:

-----Объектные типы данных
--Расширяют реляционную модель
--Могут объединять данные и операции над ними
--Могут эффективно использоваться
--Могут показывать взаимосвязь и наследование данных


--a.	Дополнительный конструктор;

create or replace type VehicleType as object (
    vehicleId NUMBER,
    driverId NUMBER,
    model VARCHAR2(100),
    vtype VARCHAR2(50),
    capacity NUMBER,
    licencePlate NUMBER,
    brand VARCHAR2(100),
    addDate DATE,
    constructor function VehicleType(
        p_vehicleId NUMBER,
        p_driverId NUMBER,
        p_model VARCHAR2
    ) return self as result,
    constructor function VehicleType(
        p_vehicleId NUMBER,
        p_driverId NUMBER,
        p_model VARCHAR2,
        p_type VARCHAR2,
        p_capacity NUMBER,
        p_licencePlate NUMBER,
        p_brand VARCHAR2,
        p_addDate DATE  
    ) return self as result
);

CREATE OR REPLACE TYPE BODY VehicleType AS
    CONSTRUCTOR FUNCTION VehicleType(
        p_vehicleId NUMBER,
        p_driverId NUMBER,
        p_model VARCHAR2
    ) RETURN SELF AS RESULT IS
    BEGIN
        SELF.vehicleId := p_vehicleId;
        SELF.driverId := p_driverId;
        SELF.model := p_model;
        SELF.vtype := 'TruckW';
        SELF.capacity := 500;
        SELF.licencePlate := 1111;
        SELF.brand := 'BMW';
        SELF.addDate := SYSDATE;
        RETURN;
    END;
        CONSTRUCTOR FUNCTION VehicleType(
        p_vehicleId NUMBER,
        p_driverId NUMBER,
        p_model VARCHAR2,
        p_type VARCHAR2,
        p_capacity NUMBER,
        p_licencePlate NUMBER,
        p_brand VARCHAR2,
        p_addDate DATE  
    ) RETURN SELF AS RESULT IS
    BEGIN
        SELF.vehicleId := p_vehicleId;
        SELF.driverId := p_driverId;
        SELF.model := p_model;
        SELF.vtype := p_type;
        SELF.capacity := p_capacity;
        SELF.licencePlate := p_licenceplate;
        SELF.brand := p_brand;
        SELF.addDate := p_adddate;
        RETURN;
    END;
END;

drop table vehicle_const;
create table vehicle_const of VehicleType;

insert into vehicle_const values(VehicleType(1,1,'VAZ 2101'));

select * from vehicle_const;


CREATE OR REPLACE TYPE OrderType AS OBJECT (
    orderId NUMBER,
    orderCargo NUMBER,
    orderVehicle NUMBER,
    price NUMBER,
    status VARCHAR2(150),
    createdAt DATE,
    orderRoute NUMBER,
    CONSTRUCTOR FUNCTION OrderType(
        p_orderId NUMBER,
        p_orderCargo NUMBER,
        p_orderVehicle NUMBER,
        p_price NUMBER,
        p_status VARCHAR2,
        p_createdAt DATE,
        p_orderRoute NUMBER
    ) RETURN SELF AS RESULT
);


CREATE OR REPLACE TYPE BODY OrderType AS
    CONSTRUCTOR FUNCTION OrderType(
        p_orderId NUMBER,
        p_orderCargo NUMBER,
        p_orderVehicle NUMBER,
        p_price NUMBER,
        p_status VARCHAR2,
        p_createdAt DATE,
        p_orderRoute NUMBER
    ) RETURN SELF AS RESULT IS
    BEGIN
        SELF.orderId := p_orderId;
        SELF.orderCargo := p_orderCargo;
        SELF.orderVehicle := p_orderVehicle;
        SELF.price := p_price;
        SELF.status := p_status;
        SELF.createdAt := p_createdAt;
        SELF.orderRoute := p_orderRoute;
        RETURN;
    END;
END;


--b.	Метод сравнения типа MAP или ORDER;
-- Методы MAP – предназначены для сравнения, сортировки и UNION
-- Методы ORDER – предназначены для сортировки по значениям полей
-- map:

create or replace type VehicleType as object (
    vehicleId NUMBER,
    driverId NUMBER,
    model VARCHAR2(100),
    type VARCHAR2(50),
    capacity NUMBER,
    licencePlate NUMBER,
    brand VARCHAR2(100),
    addDate DATE,
    map member function get_id_no return varchar2
);


CREATE OR REPLACE TYPE BODY VehicleType AS
    MAP MEMBER FUNCTION get_id_no RETURN VARCHAR2 IS
    BEGIN
        RETURN vehicleId;
    END;
END;

drop type body VehicleType;

create table vehicle_map(
 vehicle VehicleType
);

insert into vehicle_map values(VehicleType(1,1,'VAZ 2101','TRUCK',200,2131231,'BMW',SYSDATE));
insert into vehicle_map values(VehicleType(2,1,'VAZ 2101','TRUCK',200,2131231,'BMW',SYSDATE));

select v.vehicle.get_id_no() from vehicle_map v;

select v1.vehicle, v2.vehicle from vehicle_map v1
join vehicle_map v2 on v1.vehicle = v2.vehicle;

drop table vehicle_map;


CREATE OR REPLACE TYPE OrderType AS OBJECT (
    orderId NUMBER,
    orderCargo NUMBER,
    orderVehicle NUMBER,
    price NUMBER,
    status VARCHAR2(150),
    createdAt DATE,
    orderRoute NUMBER,
    order member function is_order (order_val OrderType) return integer
);

create or replace type body OrderType as
order member function is_order(order_val OrderType) return integer is
begin
    if price > order_val.price
        then return -1;
    elsif price < order_val.price
        then return 1;
    else return 0;
    end if;
end;
end;

drop table order_ord;
create table order_ord of OrderType;

INSERT INTO order_ord VALUES (
    OrderType(1, 100, 10, 500.00, 'Pending', SYSDATE, 1)
);


SELECT a.is_order(OrderType(2, 100, 10, 600, 'Completed', SYSDATE, 1)) AS result
FROM order_ord a
WHERE a.orderId = 1;



--c.	Метод экземпляра функцию;


CREATE OR REPLACE TYPE OrderType AS OBJECT (
    orderId NUMBER,
    orderCargo NUMBER,
    orderVehicle NUMBER,
    price NUMBER,
    status VARCHAR2(150),
    createdAt DATE,
    orderRoute NUMBER,
    member function get_description return VARCHAR2
);



CREATE OR REPLACE TYPE BODY OrderType AS
    MEMBER FUNCTION get_description RETURN VARCHAR2 IS
    BEGIN
        RETURN 'Order ID: ' || orderId || ', Status: ' || status;
    END;
END;


drop table order_ord;
create table order_ord of OrderType;

INSERT INTO order_ord VALUES (
    OrderType(1, 100, 10, 500.00, 'Pending', SYSDATE, 1)
);

SELECT o.get_description() AS order_description
FROM order_ord o;




--d.	Метод экземпляра процедуру.



create or replace type VehicleType as object (
    vehicleId NUMBER,
    driverId NUMBER,
    model VARCHAR2(100),
    type VARCHAR2(50),
    capacity NUMBER,
    licencePlate NUMBER,
    brand VARCHAR2(100),
    addDate DATE,
    member procedure update_model(p_model VARCHAR2)
);

CREATE OR REPLACE TYPE BODY VehicleType AS
    MEMBER PROCEDURE update_model(p_model VARCHAR2) IS
    BEGIN
        SELF.model := p_model;
    END;
END;

drop table vehicle_map;
create table vehicle_map of VehicleType;

declare
    vehicle_j VehicleType;
begin
    vehicle_j := NEW VehicleType(1,1,'VAZ 2101','TRUCK',200,2131231,'BMW',SYSDATE);
    vehicle_j.update_model('BMW I8');
    insert into vehicle_map values(vehicle_j);
end;
select * from vehicle_map;

--3.	Скопировать данные из реляционных таблиц в объектные.

create or replace type VehicleType as object (
    vehicleId NUMBER,
    driverId NUMBER,
    model VARCHAR2(100),
    type VARCHAR2(50),
    capacity NUMBER,
    licencePlate NUMBER,
    brand VARCHAR2(100),
    addDate DATE,
    member function get_id_no return NUMBER deterministic
);


CREATE OR REPLACE TYPE BODY VehicleType AS
    MEMBER FUNCTION get_id_no RETURN NUMBER deterministic IS
    BEGIN
        RETURN vehicleId;
    END;
END;


CREATE OR REPLACE TYPE OrderType AS OBJECT (
    orderId NUMBER,
    orderCargo NUMBER,
    orderVehicle NUMBER,
    price NUMBER,
    status VARCHAR2(150),
    createdAt DATE,
    orderRoute NUMBER
);


create table vehicle_object(
vehicle VehicleType
);
INSERT INTO vehicle_object(vehicle)
SELECT VehicleType(vehicleId, driverId, model, type, capacity, licencePlate, brand, addDate)
FROM Vehicles;

select * from vehicle_object;

create table order_object of OrderType;
INSERT INTO order_object
SELECT OrderType(orderId, orderCargo, orderVehicle, price, status, createdAt, orderRoute)
FROM Orders;


select * from order_object;

commit;

drop table vehicle_object;
drop table order_object;

--4.	Продемонстрировать применение объектных представлений.

CREATE OR REPLACE VIEW VehicleObjectView OF VehicleType
WITH OBJECT IDENTIFIER (vehicleId) AS
SELECT VehicleType(vehicleId, driverId, model, type, capacity, licencePlate, brand, addDate)
FROM Vehicles;



CREATE OR REPLACE VIEW OrderObjectView OF OrderType
WITH OBJECT IDENTIFIER (orderId) AS
SELECT OrderType(orderId, orderCargo, orderVehicle, price, status, createdAt, orderRoute)
FROM Orders;


SELECT * FROM VehicleObjectView;
SELECT VALUE(o) FROM OrderObjectView o;


--5.	Продемонстрировать применение индексов для индексирования по атрибуту и по методу в объектной таблице.
select * from vehicle_object;


select * from vehicle_object v where v.vehicle.BRAND = 'Mercedes-Benz';
CREATE INDEX idx_vehicle_BRAND ON vehicle_object (vehicle.BRAND);

select * from vehicle_object v where v.vehicle.get_id_no() = 1;
CREATE BITMAP INDEX idx_vehicle_get_id_no ON vehicle_object (vehicle.get_id_no());
