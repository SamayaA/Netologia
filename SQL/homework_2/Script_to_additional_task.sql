CREATE TABLE IF NOT EXISTS employee (
id serial not null primary key ,
name varchar (80) not null
);

CREATE TABLE IF NOT EXISTS department (
id serial not null primary key ,
title varchar (80) not null
);

CREATE TABLE IF NOT EXISTS department_head (
department_id integer references department(id),
employee_id integer references employee(id)
);