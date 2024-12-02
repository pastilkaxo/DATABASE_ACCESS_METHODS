INSERT INTO Roles (roleName) VALUES ('admin');
INSERT INTO Roles (roleName) VALUES ('driver');
INSERT INTO Roles (roleName) VALUES ('shipper');

INSERT INTO Users (firstName, lastName, fatherName, email, password, phone, role, INN, userType, verified)
VALUES ('Cristiano', 'Ronaldo', NULL, 'cr7.example@.com', 'cr7isgood', '80291313441', 2, 'HFEHA233KE', 'Юрид. лицо', 1);

INSERT INTO Users (firstName, lastName, fatherName, email, password, phone, role, INN, userType, verified)
VALUES ('Vladislav', 'Lemiashusky', 'Olegovich', 'vlad.lemeshok@gmail.com', 'qwerty12345', '80290384288', 3, 'FFEJ324BBJE', 'Юрид. лицо', 1);

INSERT INTO Users (firstName, lastName,fatherName, email, password, phone, role, INN, userType, verified)
VALUES ('Lionel', 'Messi', NULL, 'messi@example.com', 'messiisgreat', '80291313442', 2, 'HFEHA233KF', 'Юрид. лицо', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Big box of apples', 50, 150, 'BOX', 'Minsk', 'Madrid', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Small box of oranges', 20, 80, 'BOX', 'Minsk', 'Barcelona', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Medium box of bananas', 30, 100, 'BOX', 'Minsk', 'Berlin', 1);

INSERT INTO Cargo (description, weight, volume, bodyType, loadingAddress, uploadingAddress, clientId)
VALUES ('Box of apples', 35, 105, 'BOX', 'Minsk', 'Moscow', 3);

INSERT INTO Vehicles (driverId, model, type, capacity, licencePlate, brand)
VALUES (2, 'Track', 'Big', 3000, '8029', 'Mercedes-Benz');

INSERT INTO Vehicles (driverId, model, type, capacity, licencePlate, brand)
VALUES (3, 'Van', 'Medium', 1500, '8030', 'Ford');

INSERT INTO Routes (distance, loadingDate, uploadingDate)
VALUES (1500, GETDATE(), GETDATE());

INSERT INTO Routes (distance, loadingDate, uploadingDate)
VALUES (1200, GETDATE(), GETDATE());

INSERT INTO Orders (orderCargo, orderVehicle, price, status, orderRoute)
VALUES (1, 1, 2500, 'completed', 1);

INSERT INTO Orders (orderCargo, orderVehicle, price, status, orderRoute)
VALUES (2, 2, 1500, 'completed', 2);

INSERT INTO Orders (orderCargo, orderVehicle, price, status, orderRoute)
VALUES (3, 1, 2000, 'completed', 1);

INSERT INTO Orders (orderCargo, orderVehicle, price, status, orderRoute)
VALUES (4, 1, 2000, 'completed', 2);

INSERT INTO Orders (orderCargo, orderVehicle, price, status, orderRoute)
VALUES (1, 2, 3000, 'completed', 2);

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 2500, 'credit_card', 'pending', '2024-03-10');

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 5000, 'credit_card', 'pending', '2024-04-25');

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 5000, 'paypal', 'completed', '2024-04-25');

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 1500, 'credit_card', 'completed', '2024-05-15');

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 2000, 'bank_transfer', 'completed', '2024-07-18');

INSERT INTO Payments (paymentOrder, amount, paymentMethod, paymentStatus, paymentDate)
VALUES (1, 2300, 'bank_transfer', 'completed', '2024-09-03');

INSERT INTO Reviews (reviewOrder, reviewerId, reviewComment, reviewedVehicle, rating)
VALUES (1, 1, 'Made fast and good', 1, 9);



-- 1. Вычисление итогов предоставленных услуг помесячно, за квартал, за полгода, за год.

SELECT 
    YEAR(paymentDate) AS year,
    MONTH(paymentDate) AS month,
    DATEPART(QUARTER, paymentDate) AS quarter,
    CASE 
        WHEN MONTH(paymentDate) BETWEEN 1 AND 6 THEN 'H1'
        WHEN MONTH(paymentDate) BETWEEN 7 AND 12 THEN 'H2'
        ELSE NULL
    END AS half_year,
    SUM(amount) AS totalAmount
FROM Payments
GROUP BY 
    ROLLUP (YEAR(paymentDate), MONTH(paymentDate)), 
    ROLLUP (YEAR(paymentDate), DATEPART(QUARTER, paymentDate)),
    ROLLUP (YEAR(paymentDate), 
        CASE WHEN MONTH(paymentDate) BETWEEN 1 AND 6 THEN 'H1'
             WHEN MONTH(paymentDate) BETWEEN 7 AND 12 THEN 'H2' END),
    YEAR(paymentDate)
ORDER BY year, month, quarter, half_year;


-- 2. Вычисление итогов предоставленных услуг для определенного вида услуги за период:
WITH ServiceSummary AS (
    SELECT 
        o.orderCargo,
        SUM(p.amount) AS total_service_amount,
        COUNT(o.orderId) AS total_orders
    FROM Orders o
    JOIN Payments p ON o.orderId = p.paymentOrder
    WHERE 
        o.orderCargo = 1
        AND p.paymentDate BETWEEN '2024-03-01' AND '2024-04-30'
    GROUP BY 
        o.orderCargo
),
TotalService AS (
    SELECT 
        SUM(p.amount) AS total_amount
    FROM Payments p
    WHERE 
        p.paymentDate BETWEEN '2024-03-01' AND '2024-06-30'
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
    ) AS sub
)
SELECT 
    ss.total_service_amount,
    (ss.total_service_amount * 100.0 / ts.total_amount) AS percent_of_total,
    (ss.total_service_amount * 100.0 / ms.max_amount) AS percent_of_max
FROM 
    ServiceSummary ss,
    TotalService ts,
    MaxService ms;


-- 3. Продемонстрируйте применение функции ранжирования ROW_NUMBER() для разбиения результатов запроса на страницы (по 20 строк на каждую страницу).

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
WHERE row_num BETWEEN 1 AND 2;


-- 4. Продемонстрируйте применение функции ранжирования ROW_NUMBER() для удаления дубликатов.

WITH RankedPayments AS (
    SELECT 
        paymentId,
        ROW_NUMBER() OVER (PARTITION BY paymentOrder, amount, paymentDate ORDER BY paymentId) AS row_num
    FROM Payments
)
DELETE FROM Payments
WHERE paymentId IN (
    SELECT paymentId
    FROM RankedPayments
    WHERE row_num > 1
);


-- 5. Вернуть для каждого клиента направления последних 6 заказов.

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


-- 6. Какой маршрут пользовался наибольшей популярностью для определенного типа автомобилей? Вернуть для всех типов.

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
