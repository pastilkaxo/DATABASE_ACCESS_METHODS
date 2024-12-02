SELECT clientId, 
       SUM(previousPrice) AS totalPreviousPrice, 
       SUM(newPrice) AS totalNewPrice
FROM (
    SELECT clientId, previousPrice, newPrice
    FROM (
        SELECT 
            c.clientId, 
            o.price AS previousPrice,
            0 AS newPrice
        FROM 
            Orders o
        JOIN 
            Cargo c ON o.orderCargo = c.cargoId
        WHERE 
            o.status = 'completed'
    ) 
    MODEL
        PARTITION BY (clientId)
        DIMENSION BY (ROWNUM AS rn)
        MEASURES (previousPrice, newPrice)
        RULES AUTOMATIC ORDER (
            newPrice[ANY] = previousPrice[CV()] * 1.10
        )
)
GROUP BY clientId;

select * from cargo

SELECT cargoId,
       previousPrice, 
       newPrice
FROM (
    SELECT 
        c.cargoId,
        o.price AS previousPrice,
        0 AS newPrice -- Инициализируем новое значение для расчета
    FROM 
        Orders o
    JOIN 
        Cargo c ON o.orderCargo = c.cargoId
    WHERE 
        o.status = 'completed'
) 
MODEL
    PARTITION BY (cargoId) -- Группировка по клиенту
    DIMENSION BY (ROWNUM AS rn) -- Используем ROWNUM как измерение
    MEASURES (previousPrice, newPrice)
    RULES AUTOMATIC ORDER (
        newPrice[ANY] = previousPrice[CV()] * 1.10 -- Применяем увеличение на 10%
    );
    
-- 2:

SELECT *
FROM (
    SELECT
        v.type AS vehicleType,
        TO_DATE(TO_CHAR(o.createdAt, 'YYYY-MM'), 'YYYY-MM') AS tstamp,
        COUNT(o.OrderId) AS ordersCount
    FROM Orders o
    JOIN Vehicles v ON o.OrderVehicle = v.VehicleId
    GROUP BY v.type, TO_DATE(TO_CHAR(o.createdAt, 'YYYY-MM'), 'YYYY-MM')
)
MATCH_RECOGNIZE (
    PARTITION BY vehicleType
    ORDER BY tstamp
    MEASURES
        FIRST(A.tstamp) AS start_period,
        LAST(B.tstamp) AS mid_period,
        LAST(C.tstamp) AS end_period,
        FIRST(A.ordersCount) AS start_orders,
        LAST(B.ordersCount) AS mid_orders,
        LAST(C.ordersCount) AS end_orders
    PATTERN (A B C)
    DEFINE
        B AS B.ordersCount < A.ordersCount,   
        C AS C.ordersCount > B.ordersCount    
);


select * from Vehicles
select * from orders

