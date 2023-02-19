-- create table items (
-- 	id int primary key,
-- 	item varchar(30),
-- 	price int
-- )

-- create table customers (
-- 	id int primary key,
-- 	First_name varchar(30),
-- 	last_name varchar(30)
-- );

-- insert into items 
-- values (1,'Small Desk',100),
-- (2,'Large Desk',300),
-- (3,'Fan',80)
-- ;

-- insert into customers 
-- values (1,'Greg ','Jones'),
-- (2,'Sandra','Jones'),
-- (3,'Scott','Scott'),
-- (4,'Trevor','Green'),
-- (5,'Melanie','Johnson')
-- ;

-- select * from items;
-- select * from items where price >80;

-- select * from items where price <300;

-- select * from customers where last_name ='Smith'; --> empty table

-- select * from customers where last_name ='Jones';

select * from customers where first_name !='Scott';