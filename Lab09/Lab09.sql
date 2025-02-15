select * from Cargo;

select * from Orders;


--2.	������������������ ��������� ������ �� ��������� ������ ��� ������ 
-- ��������� ��������� ������� 
--�� �������� (� ������ �������� ������ ������� t1, ������ � t2):
--a.	������� ��������� �� ������ t1, ����� K1, ��� ��� ��� ������� � ��������� 
--��������� �� ������ t2, ����� �2;


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
-- ������
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


-- �����

for i in 1..ck1.count loop
    dbms_output.put_line('a. ����: ' || ck1(i).cargoId || ', ��������: ' 
    || ck1(i).description || ', �������: ' || ck1(i).orders.COUNT);
end loop;


--b.	�������� ��� ����� ��������� �1 ��������� �2 ������������;

for i in 1..ck1.COUNT loop
    for j in i+1..ck1.COUNT loop
        for k in 1..ck1(i).orders.COUNT loop
            for m in 1..ck1(j).orders.COUNT loop
                   IF ck1(i).orders(k).orderVehicle = ck1(j).orders(m).orderVehicle OR 
                      ck1(i).orders(k).orderRoute = ck1(j).orders(m).orderRoute THEN
                       DBMS_OUTPUT.PUT_LINE('! ����������� ! ����� ' 
                            || ck1(i).cargoId || ' � ' || ck1(j).cargoId 
                            || ' ����� ����� ' || 
                            CASE 
                                WHEN ck1(i).orders(k).orderVehicle = ck1(j).orders(m).orderVehicle THEN '���������: ' || ck1(i).orders(k).orderVehicle
                                ELSE '�������: ' || ck1(i).orders(k).orderRoute
                            END);
                   END IF;
            end loop;
        end loop;
    end loop;
end loop;


--c.	��������, �������� �� ������ ��������� �1 �����-�� ������������ �������;

for i in 1..ck1.COUNT loop
    if ck1(i).cargoId = c_cargo_id then
        DBMS_OUTPUT.PUT_LINE('c. ���� � ID: ' || c_cargo_id || ' ������ � K1');
        exit;
    else
        DBMS_OUTPUT.PUT_LINE('c. ���� � ID: ' || c_cargo_id || '�� ������ � K1');
    end if;
    
    
end loop;

--d.	����� ������ ��������� �1;

for i in 1..ck1.COUNT loop
    if ck1(i).orders.COUNT = 0 then
        DBMS_OUTPUT.PUT_LINE('d. ���� ID ' || ck1(i).cargoId || ' �� ����� ������� (������ ��������� K2).');
    end if;
end loop;


--e.	��� ���� ��������� ��������� �1 �������� �� �������� �2. 
DBMS_OUTPUT.PUT_LINE('E: BEFORE');
DBMS_OUTPUT.PUT_LINE('���� 1: ' || ck1(1).cargoId || 
', �����: ' || ck1(1).orders(1).orderId || 
', �������: ' || ck1(1).orders(1).orderRoute);
DBMS_OUTPUT.PUT_LINE('���� 2: ' || ck1(4).cargoId || 
', �����: ' || ck1(4).orders(1).orderId || 
', �������: ' || ck1(4).orders(1).orderRoute);
                                                       
                                
temp_order := ck1(1).orders(1).orderRoute;
ck1(1).orders(1).orderRoute := ck1(4).orders(1).orderRoute;
ck1(4).orders(1).orderRoute := temp_order;

DBMS_OUTPUT.PUT_LINE('AFTER');
DBMS_OUTPUT.PUT_LINE('���� 1: ' || ck1(1).cargoId || 
', �����: ' || ck1(1).orders(1).orderId || 
', �������: ' || ck1(1).orders(1).orderRoute);
DBMS_OUTPUT.PUT_LINE('���� 2: ' || ck1(4).cargoId || 
', �����: ' || ck1(4).orders(1).orderId || 
', �������: ' || ck1(4).orders(1).orderRoute);


--3.	������������� ��������� � ������� ����.

for i in 1..ck1.COUNT LOOP
    for j in 1..ck1(i).orders.COUNT loop
        insert into tt1(orderId,orderCargo,price,orderVehicle)
        values (ck1(i).orders(j).orderId,ck1(i).orders(j).orderCargo,ck1(i).orders(j).price,ck1(i).orders(j).orderVehicle);
    end loop;
end loop;
DBMS_OUTPUT.PUT_LINE('������ �������������!');

--4.	������������������ ���������� BULK �������� �� ������� ����� ���������.

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