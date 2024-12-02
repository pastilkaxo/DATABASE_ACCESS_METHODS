use mshoad


-- 1.	��� ���� ������ � ���� SQL Server �������� ��� ����� �� ������ ������� ������ �������������� ����. 

alter table Users add parentUserID int; 


-- 2.	������� ���������, ������� ��������� ��� ����������� ���� � ��������� ������ �������� (�������� � �������� ����).
select * from Users

drop procedure GetUserParents;

create procedure GetUserParents 
(
@userId int
)
as
begin
    WITH UserLevels AS (
        SELECT 
            userId, 
            firstName, 
            lastName, 
            parentUserId, 
            0 AS 'level' 
        FROM Users
        WHERE userId = @userId
        UNION ALL
        SELECT 
            u.userId, 
            u.firstName, 
            u.lastName, 
            u.parentUserId, 
            ul.level + 1 
        FROM Users u
        INNER JOIN UserLevels ul ON u.parentUserId = ul.userId
    )
    SELECT 
        userId, 
        firstName, 
        lastName, 
        level
    FROM UserLevels
    ORDER BY level, userId;
end;

exec GetUserParents @userId = 1;


-- 3.	������� ���������, ������� ������� ����������� ���� (�������� � �������� ����).

drop procedure AddUsersToLevel;

create procedure AddUsersToLevel
	@fName varchar(255),
	@lName varchar(255),
	@faName varchar(255) = NULL,
	@em varchar(255),
	@pass varchar(255),
	@tel varchar(25),
	@rId int,
	@inn varchar(50),
	@uType varchar(150),
	@vf BIT,
	@parentUserId int = NULL
as
insert into Users (firstName,lastName,fatherName,email,password,phone,role,INN,userType,verified,parentUserID)
values
(@fName,@lName,@faName,@em,@pass,@tel,@rId,@inn,@uType,@vf , @parentUserId)
;


exec AddUsersToLevel 'Travis', 'Scott' , null,
'exmaple@gmail.com','qwertobobob','80299876655',2,'FEFEIW123WIE','��',1,2;

exec GetUserParents @userId = 1;


-- 4.	������� ���������, ������� ���������� ��� ����������� ����� (������ �������� � �������� �������� ������������� ����, 
--		������ �������� � �������� ����, � ������� ���������� �����������).


drop procedure MoveLevel;

create procedure MoveLevel
(
@mainId int,
@targetId int
)
as
	update Users set parentUserID = @targetId  
	where  userId = @mainId or parentUserID = @mainId
;

exec MoveLevel 3,1;

select * from Users;
