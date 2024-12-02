
SELECT * FROM capitals


SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA

select * from geometry_columns

--geometry -  ��� ������ ������������ ��� ������������� ���������������� �������� � ���������

-- 6.	���������� ��� ���������������� ������ �� ���� ��������
--  �������������� �������� � ������������
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'dbo' and DATA_TYPE='geometry'
--
-- 7.	���������� SRID - ������������� ������� ���������
-- WGS 84 (������/�������)
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'rivers' AND DATA_TYPE = 'geometry'

select distinct geom.STSrid as srid from capitals

SELECT	srid FROM geometry_columns




-- 8.	���������� ������������ �������
-- �������������� �������������� ��������
SELECT TABLE_NAME,COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'dbo' AND DATA_TYPE != 'geometry' and TABLE_NAME in ('capitals','countries','lakes','rivers','ocean');

-- 9.	������� �������� ���������������� �������� � ������� WKT
--  ��������� ������ 

SELECT name,geom.STAsText() FROM rivers;


-- 10 
-- WHERE c1.qgs_fid = 1 AND c2.qgs_fid = 2
select * from capitals

-- 10.1.	���������� ����������� ���������������� ��������;
-- ����������� �������, ����� ��� ���� ��� ����� ���������������� ��������.

SELECT c1.qgs_fid, c2.qgs_fid, c1.geom.STIntersection(c2.geom).STAsText() AS �����������
FROM countries c1, capitals c2
WHERE c1.geom.STIntersects(c2.geom) = 1
;

-- 10.2.	���������� ����������� ���������������� ��������;
SELECT c1.qgs_fid, c2.qgs_fid, c1.geom.STUnion(c2.geom).STAsText() AS �����������
FROM lakes c1, rivers c2;

-- 10.3.	���������� ����������� ���������������� ��������;

SELECT c1.qgs_fid, c2.qgs_fid, c1.geom.STWithin(c2.geom) AS ��������
FROM countries c1, capitals c2;

-- 10.4.	��������� ����������������� �������;
-- ���������� ��������� ��������� ������� � ����������� ��� �������� �������������


SELECT qgs_fid, geom.Reduce(0.1).STAsText() AS ���������
FROM rivers;

-- 10.5.	���������� ��������� ������ ����������������� ��������

SELECT qgs_fid ,geom.STPointN(2).STAsText() AS �������
FROM rivers;

-- 10.6.	���������� ����������� ���������������� ��������
--   ����� ����� ����������� 0, ����� - 1, � ������� - 2.

SELECT qgs_fid,name,geom.STDimension() AS ����������� 
FROM capitals
union all
SELECT qgs_fid,name,geom.STDimension() AS ����������� 
FROM rivers
union all
SELECT qgs_fid,name,geom.STDimension() AS �����������
FROM countries;

-- 10.7.	���������� ����� � ������� ���������������� ��������;

SELECT qgs_fid,  geom.STLength() AS �����, geom.STArea() as �������
FROM lakes;


-- 10.8.	���������� ���������� ����� ����������������� ���������;

SELECT  c1.qgs_fid , c2.qgs_fid, c1.geom.STDistance(c2.geom) AS ����������
FROM capitals c1, capitals c2;

-- 11.	�������� ���������������� ������ � ���� ����� (1) /����� (2) /�������� (3).
-- �����


INSERT INTO capitals (geom,name)
VALUES (geometry::STPointFromText('POINT (37.5646813 63.9019233)', 4326),'VladLand');

select * from capitals where qgs_fid = 246;

delete from capitals where qgs_fid = 246;


-- �����


INSERT INTO rivers (geom,name)
VALUES (geometry::STLineFromText('LINESTRING(29.1 55.1, 29.4 55.4)', 4326),'VladRiver');

select * from rivers where qgs_fid = 19;

delete from rivers where qgs_fid = 19;

-- �������

INSERT INTO lakes (geom,name)
VALUES (geometry::STGeomFromText('POLYGON ((29.0 55.5, 29.5 55.5, 29.5 55.0, 29.0 55.0, 29.0 55.5))',4326),'VladLake'); 


select * from lakes where qgs_fid = 26;

delete from lakes where qgs_fid = 25;

-- 12.	�������, � ����� ���������������� ������� �������� ��������� ���� �������


-- �����
SELECT *
FROM countries
WHERE geom.STContains(geometry::STPointFromText('POINT (37.5646813 63.9019233)', 4326)) = 1;

-- �����
SELECT *
FROM lakes
WHERE geom.STContains(geometry::STLineFromText('LINESTRING(29.1 55.1, 29.4 55.4)', 4326)) = 1;

-- �������

SELECT *
FROM countries
WHERE geom.STContains(geometry::STGeomFromText('POLYGON ((29.0 55.5, 29.5 55.5, 29.5 55.0, 29.0 55.0, 29.0 55.5))',4326)) = 1;