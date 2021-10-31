create table categories
(
	category_id serial primary key,
	category_title varchar(255) not null,
	category_description text not null
);

create table products
(
	product_id serial primary key,
	product_title varchar(255) not null,
	product_description text not null,
	in_stock integer not null,
	price double precision not null,
	slug varchar(255) not null,
	category_id integer not null,
	foreign key (category_id) references categories (category_id)
);
 
create table users
(
	user_id serial primary key,
	email varchar(255) not null,
	password varchar(255) not null,
	first_name varchar(255) not null,
	last_name varchar(255) not null,
	middle_name varchar(255) not null,
	is_staff boolean not null,
	country varchar(255) not null,
	city varchar(255) not null,
	address text not null,
	phone_number varchar(10)
);

create table carts
(
	cart_id serial primary key,
	user_id integer not null,
	subtotal numeric not null,
	total numeric not null,
	timestamp timestamp(2) not null,
	foreign key (user_id) references users (user_id)
);

create table order_status
(
	order_status_id serial primary key,
	status_name varchar(255) not null
);

create table orders
(
	order_id serial primary key,
	cart_id integer not null,
	order_status_id integer not null,
	shipping_total numeric,
	total numeric,
	created_at timestamp(2) not null,
	updated_at timestamp(2) not null,
	foreign key (cart_id) references carts (cart_id),
	foreign key (order_status_id) references order_status (order_status_id)
);

create table cart_product
(
	cart_id integer not null,
	product_id integer not null,
	primary key (cart_id, product_id),
	foreign key (cart_id) references carts (cart_id),
	foreign key (prduct_id) references products (product_id)
);

ALTER TABLE users ADD COLUMN phone_number INT;

ALTER TABLE users ALTER COLUMN phone_number TYPE varchar(10);

UPDATE products SET price = price * 2