CREATE DATABASE public OWNER = postgres ENCODING = 'UTF8' CONNECTION LIMIT = 100;

CREATE TABLE items (id SERIAL PRIMARY KEY, item_name VARCHAR(100), item_price INTEGER);

CREATE TABLE customers (id SERIAL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50));

INSERT INTO items (item_name,item_price)
VALUES ('Small Desk' ,100), ( 'Large Desk' ,300),( 'Fan' ,80)

INSERT INTO customers (first_name,last_name)
VALUES ('Greg' , 'Jones'), ( 'Sandra' , 'Jones'),( 'Scott' , 'Scott'),( 'Trevor' , 'Green'),( 'Melanie' , 'Johnson');

SELECT * FROM public.items

SELECT * FROM public.items WHERE item_price>80

SELECT * FROM public.items WHERE item_price<300

SELECT * FROM public.customers WHERE last_name='Smith'
-- returns an empty table

SELECT * FROM public.customers WHERE last_name='Jones'

SELECT * FROM public.customers WHERE last_name<>'Scott'