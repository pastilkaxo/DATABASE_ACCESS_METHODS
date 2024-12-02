select * from Users;

-- 1. Column

alter table Users add parentUserID number;

-- 2.	—оздать процедуру, котора€ отобразит все подчиненные узлы с указанием уровн€ иерархии (параметр Ц значение узла).

create or replace procedure GetUserParents
(
userIDF number
)
as
cursor user_curs is 
    select LEVEL,  userId , firstName , lastName , parentUserID from Users
    start with userId = userIDF
    connect by prior userId = parentUserID
    order by LEVEL
    ; 
begin
    for ur in user_curs loop
        DBMS_OUTPUT.PUT_LINE('Level: ' || ur.LEVEL || ', UserId: ' || ur.userId || ', FirstName: ' || ur.firstName || 
        ', LastName: ' || ur.lastName || ', Parent: ' || COALESCE(TO_CHAR(ur.parentUserID), 'NULL'));
    end loop;
end;


begin
    GetUserParents(1);
end;


-- 3.	—оздать процедуру, котора€ добавит подчиненный узел (параметр Ц значение узла).


drop procedure AddUsersToLevel;

create or replace procedure AddUsersToLevel (
	fName varchar,
	lName varchar,
	faName varchar,
	em varchar,
	pass varchar,
	tel varchar,
	rId number,
	inn varchar,
	uType varchar,
	vf number,
	parentUID number
    )
as
begin
insert into Users (firstName,lastName,fatherName,email,password,phone,role,INN,userType,verified,parentUserID)
values
(fName,lName,faName,em,pass,tel,rId,inn,uType,vf , parentUID)
;
commit;
end;

begin
 AddUsersToLevel('Travis', 'Scott' , null,
'exmaple@gmail.com','qwertobobob','80299876655',2,'FEFEIW123WIE','»ѕ',1,2);
 GetUserParents(1);
end;


-- 4.	—оздать процедуру, котора€ переместит всю подчиненную ветку (первый параметр Ц значение верхнего перемещаемого узла, 
--      второй параметр Ц значение узла, в который происходит перемещение).

drop procedure MoveLevel;

create or replace procedure MoveLevel
(
mainId number,
targetId number
)
as
begin
	update Users set parentUserID = targetId  
	where  userId = mainId or parentUserID = mainId
;
commit;
end;


begin
MoveLevel(2,3);
end;


begin
    GetUserParents(3);
end;
