use mshoad
go

EXEC sp_configure 'clr enabled', 1;
RECONFIGURE;
GO
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
GO
EXEC sp_configure 'clr strict security', 0;
RECONFIGURE;

ALTER DATABASE mshoad SET TRUSTWORTHY ON;


-- CLR 
CREATE ASSEMBLY ClrEmailNotification
FROM 'C:\Users\Влад\Desktop\МСОХАД\DATABASE_ACCESS_METHODS\Lab10\ClassLibrary1\ClassLibrary1\bin\Debug\ClassLibrary1.dll'
WITH PERMISSION_SET = UNSAFE;
go

drop assembly ClrEmailNotification;


CREATE PROCEDURE SendEmailOnDelete
AS EXTERNAL NAME ClrEmailNotification.[ClassLibrary1.Class1].SendEmailOnDelete;
go

exec SendEmailOnDelete

drop procedure SendEmailOnDelete


CREATE TYPE RouteType
EXTERNAL NAME ClrEmailNotification.[ClassLibrary1.RouteType];

drop type Routetype

DELETE FROM Routes WHERE routeId = 1;


select * from Routes;
insert into Routes
values
(1500,GETDATE() , GETDATE());


CREATE PROCEDURE DeleteRouteById
    @routeId RouteType
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (SELECT 1 FROM Routes WHERE routeId = @routeId.GetValue())
    BEGIN
        DELETE FROM Routes WHERE routeId = @routeId.GetValue();
        EXEC SendEmailOnDelete;
    END
    ELSE
    BEGIN
        PRINT 'Маршрут с таким ID не найден.';
    END
END;
GO


drop procedure DeleteRouteById


DECLARE @id RouteType;
SET @id = CAST('3' AS RouteType); 
EXEC DeleteRouteById @id;

