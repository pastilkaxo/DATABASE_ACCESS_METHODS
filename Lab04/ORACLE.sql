

-- 1. Вычисление итогов предоставленных услуг помесячно, за квартал, за полгода, за год.

SELECT 
    TO_CHAR(paymentDate, 'YYYY') AS year,
    TO_CHAR(paymentDate, 'MM') AS month,
    TO_CHAR(paymentDate, 'Q') AS quarter,
    CASE 
        WHEN TO_CHAR(paymentDate, 'MM') BETWEEN '01' AND '06' THEN 'H1'
        WHEN TO_CHAR(paymentDate, 'MM') BETWEEN '07' AND '12' THEN 'H2'
        ELSE NULL
    END AS half_year,
    SUM(amount) AS totalAmount
FROM Payments
GROUP BY 
    GROUPING SETS (
        (TO_CHAR(paymentDate, 'YYYY'), TO_CHAR(paymentDate, 'MM')),  -- Помесячно
        (TO_CHAR(paymentDate, 'YYYY'), TO_CHAR(paymentDate, 'Q')),   -- Поквартально
        (TO_CHAR(paymentDate, 'YYYY'), 
         CASE WHEN TO_CHAR(paymentDate, 'MM') BETWEEN '01' AND '06' THEN 'H1'
              WHEN TO_CHAR(paymentDate, 'MM') BETWEEN '07' AND '12' THEN 'H2' END), -- Полугодие
        (TO_CHAR(paymentDate, 'YYYY'))                               -- По годам
    )
ORDER BY year, month, quarter, half_year;



-- 2. Вычисление итогов предоставленных услуг для определенного вида услуги за период:
/*
•	объем услуг;
•	сравнение их с общим объемом услуг (в %);
•	сравнение с наибольшим объемом услуг (в %).
*/

WITH ServiceSummary AS (
    SELECT 
        o.orderCargo,
        SUM(p.amount) AS total_service_amount,
        COUNT(o.orderId) AS total_orders
    FROM Orders o
    JOIN Payments p ON o.orderId = p.paymentOrder
    WHERE 
        o.orderCargo = 1 
        AND p.paymentDate BETWEEN TO_DATE('2024-03-01', 'YYYY-MM-DD') AND TO_DATE('2024-04-30', 'YYYY-MM-DD')
    GROUP BY 
        o.orderCargo
),
TotalService AS (
    SELECT 
        SUM(p.amount) AS total_amount
    FROM Payments p
    WHERE 
        p.paymentDate BETWEEN TO_DATE('2024-03-01', 'YYYY-MM-DD') AND TO_DATE('2024-06-30', 'YYYY-MM-DD')
),
MaxService AS (
    SELECT 
        MAX(total_service_amount) AS max_amount
    FROM (
        SELECT 
            o.orderCargo,
            SUM(p.amount) AS total_service_amount
        FROM Orders o
        JOIN Payments p ON o.orderId = p.paymentOrder
        GROUP BY o.orderCargo
    )
)
SELECT 
    ss.total_service_amount,
    (ss.total_service_amount / ts.total_amount * 100) AS percent_of_total,
    (ss.total_service_amount / ms.max_amount * 100) AS percent_of_max
FROM 
    ServiceSummary ss,
    TotalService ts,
    MaxService ms;



-- 3. Продемонстрируйте применение функции ранжирования ROW_NUMBER() для разбиения результатов запроса на страницы (по 20 строк на каждую страницу).

select * from Payments order by paymentDate ;

WITH NumberedPayments AS (
    SELECT 
        paymentId,
        amount,
        paymentDate,
        paymentMethod,
        paymentStatus,
        ROW_NUMBER() OVER (ORDER BY paymentDate) AS row_num
    FROM Payments
)
SELECT *
FROM NumberedPayments
WHERE row_num BETWEEN ((:page_number - 1) * 2 + 1) AND (:page_number * 2);


-- 4. Продемонстрируйте применение функции ранжирования ROW_NUMBER() для удаления дубликатов.

select * from Payments order by paymentId;

DELETE FROM Payments
WHERE paymentId IN (
    SELECT paymentId
    FROM (
        SELECT 
            paymentId,
            ROW_NUMBER() OVER (PARTITION BY paymentOrder, amount, paymentDate ORDER BY paymentId) AS row_num
        FROM Payments
    ) sub
    WHERE row_num > 1
);


-- 6. Вернуть для каждого клиента направления последних 6 заказов.

WITH RankedOrders AS (
    SELECT 
        o.orderId,
        o.orderCargo,
        o.orderVehicle,
        o.price,
        o.status,
        o.orderRoute,
        o.createdAt,
        u.userId AS clientId,
        ROW_NUMBER() OVER (PARTITION BY u.userId ORDER BY o.createdAt DESC) AS row_num
    FROM Orders o
    INNER JOIN Cargo c ON o.orderCargo = c.cargoId
    INNER JOIN Users u ON c.clientId = u.userId
)
SELECT 
    ro.orderId,
    ro.orderCargo,
    ro.orderVehicle,
    ro.price,
    ro.status,
    ro.orderRoute,
    ro.createdAt,
    ro.clientId
FROM RankedOrders ro
WHERE ro.row_num <= 6
ORDER BY ro.clientId, ro.createdAt DESC;


-- 7:  Какой маршрут пользовался наибольшей популярностью для определенного типа автомобилей? Вернуть для всех типов.

WITH RoutePopularity AS (
    SELECT 
        v.type AS vehicleType,
        r.routeId,
        COUNT(o.orderId) AS orderCount,
        ROW_NUMBER() OVER (PARTITION BY v.type ORDER BY COUNT(o.orderId) DESC) AS rank
    FROM Orders o
    JOIN Vehicles v ON o.orderVehicle = v.vehicleId
    JOIN Routes r ON o.orderRoute = r.routeId
    GROUP BY v.type, r.routeId
)
SELECT 
    rp.vehicleType,
    rp.routeId,
    rp.orderCount
FROM RoutePopularity rp
WHERE rp.rank = 1
ORDER BY rp.vehicleType;



