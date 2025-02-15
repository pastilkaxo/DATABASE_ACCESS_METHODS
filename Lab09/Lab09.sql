select * from Cargo;

select * from Orders;


--2.	Продемонстрировать обработку данных из объектных таблиц при помощи 
-- коллекций следующим образом 
--по варианту (в каждом варианте первая таблица t1, вторая – t2):
--a.	Создать коллекцию на основе t1, далее K1, для нее как атрибут – вложенную 
--коллекцию на основе t2, далее К2;


create or replace type OrderType as object (
    orderId NUMBER,
    orderCargo NUMBER,
    price NUMBER(10,2),
    orderVehicle number ,
    orderRoute number 
);

create or replace type K2 as table of OrderType;

drop type CargoType force


create or replace type CargoType as object (
    cargoId NUMBER,
    description VARCHAR2(255),
    orders K2
);


create or replace type K1 as table of CargoType;


declare
   ck1 K1;
   c_cargo_id NUMBER := 1;
   temp_order number;
begin
-- данные
    SELECT CargoType(
               c.cargoId, 
               c.description, 
               CAST(MULTISET(
                   SELECT OrderType(o.orderId, o.orderCargo, o.price,o.orderVehicle,o.orderRoute)
                   FROM Orders o
                   WHERE o.orderCargo = c.cargoId
               ) AS K2)
           ) 
    BULK COLLECT INTO ck1 
    FROM Cargo c;


-- вывод

for i in 1..ck1.count loop
    dbms_output.put_line('a. Груз: ' || ck1(i).cargoId || ', Название: ' 
    || ck1(i).description || ', Заказов: ' || ck1(i).orders.COUNT);
end loop;


--b.	Выяснить для каких коллекций К1 коллекции К2 пересекаются;

for i in 1..ck1.COUNT loop
    for j in i+1..ck1.COUNT loop
        for k in 1..ck1(i).orders.COUNT loop
            for m in 1..ck1(j).orders.COUNT loop
                   IF ck1(i).orders(k).orderVehicle = ck1(j).orders(m).orderVehicle OR 
                      ck1(i).orders(k).orderRoute = ck1(j).orders(m).orderRoute THEN
                       DBMS_OUTPUT.PUT_LINE('! Пересечение ! Грузы ' 
                            || ck1(i).cargoId || ' и ' || ck1(j).cargoId 
                            || ' имеют общий ' || 
                            CASE 
                                WHEN ck1(i).orders(k).orderVehicle = ck1(j).orders(m).orderVehicle THEN 'Транспорт: ' || ck1(i).orders(k).orderVehicle
                                ELSE 'Маршрут: ' || ck1(i).orders(k).orderRoute
                            END);
                   END IF;
            end loop;
        end loop;
    end loop;
end loop;


--c.	Выяснить, является ли членом коллекции К1 какой-то произвольный элемент;

for i in 1..ck1.COUNT loop
    if ck1(i).cargoId = c_cargo_id then
        DBMS_OUTPUT.PUT_LINE('c. Груз с ID: ' || c_cargo_id || ' найден в K1');
        exit;
    else
        DBMS_OUTPUT.PUT_LINE('c. Груз с ID: ' || c_cargo_id || 'не найден в K1');
    end if;
    
    
end loop;

--d.	Найти пустые коллекции К1;

for i in 1..ck1.COUNT loop
    if ck1(i).orders.COUNT = 0 then
        DBMS_OUTPUT.PUT_LINE('d. Груз ID ' || ck1(i).cargoId || ' не имеет заказов (пустая коллекция K2).');
    end if;
end loop;


--e.	Для двух элементов коллекции К1 обменять их атрибуты К2. 
DBMS_OUTPUT.PUT_LINE('E: BEFORE');
DBMS_OUTPUT.PUT_LINE('Груз 1: ' || ck1(1).cargoId || 
', Заказ: ' || ck1(1).orders(1).orderId || 
', Маршрут: ' || ck1(1).orders(1).orderRoute);
DBMS_OUTPUT.PUT_LINE('Груз 2: ' || ck1(4).cargoId || 
', Заказ: ' || ck1(4).orders(1).orderId || 
', Маршрут: ' || ck1(4).orders(1).orderRoute);
                                                       
                                
temp_order := ck1(1).orders(1).orderRoute;
ck1(1).orders(1).orderRoute := ck1(4).orders(1).orderRoute;
ck1(4).orders(1).orderRoute := temp_order;

DBMS_OUTPUT.PUT_LINE('AFTER');
DBMS_OUTPUT.PUT_LINE('Груз 1: ' || ck1(1).cargoId || 
', Заказ: ' || ck1(1).orders(1).orderId || 
', Маршрут: ' || ck1(1).orders(1).orderRoute);
DBMS_OUTPUT.PUT_LINE('Груз 2: ' || ck1(4).cargoId || 
', Заказ: ' || ck1(4).orders(1).orderId || 
', Маршрут: ' || ck1(4).orders(1).orderRoute);


--3.	Преобразовать коллекцию к другому виду.

for i in 1..ck1.COUNT LOOP
    for j in 1..ck1(i).orders.COUNT loop
        insert into tt1(orderId,orderCargo,price,orderVehicle)
        values (ck1(i).orders(j).orderId,ck1(i).orders(j).orderCargo,ck1(i).orders(j).price,ck1(i).orders(j).orderVehicle);
    end loop;
end loop;
DBMS_OUTPUT.PUT_LINE('Данные преобразованы!');

--4.	Продемонстрировать применение BULK операций на примере своих коллекций.

-- bulk insert

forall j in 1..ck1.COUNT
        insert into c1(cargoId,description)
        values (ck1(j).cargoId,ck1(j).description);
DBMS_OUTPUT.PUT_LINE('BULK INSERT DONE');

-- update 
forall j in 1..ck1.COUNT
    update c1 set description = 'NEW'
    where ck1(j).cargoId = cargoId;
DBMS_OUTPUT.PUT_LINE('BULK UPDATE DONE');
-- delete

for i in 1..ck1.COUNT loop
    forall j in indices of ck1(i).orders
        delete from tt1
        where price < 5000 and orderId = ck1(i).orders(j).orderId ;
end loop;

DBMS_OUTPUT.PUT_LINE('BULK DELETE DONE');

end;


create table tt1 (
    orderId NUMBER,
    orderCargo NUMBER,
    price NUMBER(10,2),
    orderVehicle number
);

create table c1  (
    cargoId NUMBER,
    description VARCHAR2(255)
);


drop table c1;
drop table tt1;

select * from tt1;
select * from c1;