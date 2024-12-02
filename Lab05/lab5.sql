
SELECT * FROM capitals


SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA

select * from geometry_columns

--geometry -  тип данных используется для представления пространственных объектов в плоскости

-- 6.	Определите тип пространственных данных во всех таблицах
--  местоположение объектов в пространстве
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'dbo' and DATA_TYPE='geometry'
--
-- 7.	Определите SRID - идентификатор системы координат
-- WGS 84 (широта/долгота)
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'rivers' AND DATA_TYPE = 'geometry'

select distinct geom.STSrid as srid from capitals

SELECT	srid FROM geometry_columns




-- 8.	Определите атрибутивные столбцы
-- характеристики географических объектов
SELECT TABLE_NAME,COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'dbo' AND DATA_TYPE != 'geometry' and TABLE_NAME in ('capitals','countries','lakes','rivers','ocean');

-- 9.	Верните описания пространственных объектов в формате WKT
--  текстовый формат 

SELECT name,geom.STAsText() FROM rivers;


-- 10 
-- WHERE c1.qgs_fid = 1 AND c2.qgs_fid = 2
select * from capitals

-- 10.1.	Нахождение пересечения пространственных объектов;
-- Определение области, общей для двух или более пространственных объектов.

SELECT c1.qgs_fid, c2.qgs_fid, c1.geom.STIntersection(c2.geom).STAsText() AS Пересечение
FROM countries c1, capitals c2
WHERE c1.geom.STIntersects(c2.geom) = 1
;

-- 10.2.	Нахождение объединения пространственных объектов;
SELECT c1.qgs_fid, c2.qgs_fid, c1.geom.STUnion(c2.geom).STAsText() AS Обьединения
FROM lakes c1, rivers c2;

-- 10.3.	Нахождение вложенности пространственных объектов;

SELECT c1.qgs_fid, c2.qgs_fid, c1.geom.STWithin(c2.geom) AS Вложенно
FROM countries c1, capitals c2;

-- 10.4.	Упрощение пространственного объекта;
-- Уменьшение сложности геометрии объекта с сохранением его основных характеристик


SELECT qgs_fid, geom.Reduce(0.1).STAsText() AS Упрощение
FROM rivers;

-- 10.5.	Нахождение координат вершин пространственного объектов

SELECT qgs_fid ,geom.STPointN(2).STAsText() AS Вершина
FROM rivers;

-- 10.6.	Нахождение размерности пространственных объектов
--   точка имеет размерность 0, линия - 1, а полигон - 2.

SELECT qgs_fid,name,geom.STDimension() AS Размерность 
FROM capitals
union all
SELECT qgs_fid,name,geom.STDimension() AS Размерность 
FROM rivers
union all
SELECT qgs_fid,name,geom.STDimension() AS Размерность
FROM countries;

-- 10.7.	Нахождение длины и площади пространственных объектов;

SELECT qgs_fid,  geom.STLength() AS Длина, geom.STArea() as Площадь
FROM lakes;


-- 10.8.	Нахождение расстояния между пространственными объектами;

SELECT  c1.qgs_fid , c2.qgs_fid, c1.geom.STDistance(c2.geom) AS Расстояние
FROM capitals c1, capitals c2;

-- 11.	Создайте пространственный объект в виде точки (1) /линии (2) /полигона (3).
-- точка


INSERT INTO capitals (geom,name)
VALUES (geometry::STPointFromText('POINT (37.5646813 63.9019233)', 4326),'VladLand');

select * from capitals where qgs_fid = 246;

delete from capitals where qgs_fid = 246;


-- линия


INSERT INTO rivers (geom,name)
VALUES (geometry::STLineFromText('LINESTRING(29.1 55.1, 29.4 55.4)', 4326),'VladRiver');

select * from rivers where qgs_fid = 19;

delete from rivers where qgs_fid = 19;

-- полигон

INSERT INTO lakes (geom,name)
VALUES (geometry::STGeomFromText('POLYGON ((29.0 55.5, 29.5 55.5, 29.5 55.0, 29.0 55.0, 29.0 55.5))',4326),'VladLake'); 


select * from lakes where qgs_fid = 26;

delete from lakes where qgs_fid = 25;

-- 12.	Найдите, в какие пространственные объекты попадают созданные вами объекты


-- точка
SELECT *
FROM countries
WHERE geom.STContains(geometry::STPointFromText('POINT (37.5646813 63.9019233)', 4326)) = 1;

-- линия
SELECT *
FROM lakes
WHERE geom.STContains(geometry::STLineFromText('LINESTRING(29.1 55.1, 29.4 55.4)', 4326)) = 1;

-- полигон

SELECT *
FROM countries
WHERE geom.STContains(geometry::STGeomFromText('POLYGON ((29.0 55.5, 29.5 55.5, 29.5 55.0, 29.0 55.0, 29.0 55.5))',4326)) = 1;