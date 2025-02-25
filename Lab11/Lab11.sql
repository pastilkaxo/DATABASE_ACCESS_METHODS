alter session set "_oracle_script"=true;

GRANT ALL PRIVILEGES to migr_repo identified by migr_repo;

ALTER USER mshoad ACCOUNT UNLOCK;
ALTER USER mshoad IDENTIFIED BY 123;

select * from geometry_columns;