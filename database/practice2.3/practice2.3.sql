create table potential_customers(
    id_potential_customers serial primary key,
    email varchar(255) unique not null,
    name varchar(255) not null,
    surname varchar(255) not null,
    second_name varchar(255) not null,
    city varchar(255) not null
);

select *
from potential_customers
where city like 'city17';

select first_name, email
from users
order by city, first_name;

select c.category_title, count(*)
from products inner join categories c on c.category_id = products.category_id
group by c.category_title
order by count(*) desc;

select product_title
from products left join cart_product cp on products.product_id = cp.product_id
where cp.product_id is null;

select distinct product_title
from ((products left join cart_product cp on products.product_id = cp.product_id)
    left join carts c on c.cart_id = cp.cart_id) left join orders o on o.cart_id = c.cart_id
where o.cart_id is null;

select product_title
from products inner join cart_product cp on products.product_id = cp.product_id
group by product_title
order by count(*) desc
limit 10;

select product_title
from ((products inner join cart_product cp on products.product_id = cp.product_id)
    inner join carts c on c.cart_id = cp.cart_id) inner join orders o on o.cart_id = c.cart_id
group by product_title
order by count(*) desc
limit 10;

select first_name, last_name
from users inner join carts c on users.user_id = c.user_id inner join orders o on c.cart_id = o.cart_id
group by first_name, last_name
order by sum(o.total) desc
limit 5;

select first_name, last_name
from users inner join carts c on users.user_id = c.user_id inner join orders o on c.cart_id = o.cart_id
group by first_name, last_name
order by count(o.order_id) desc
limit 5;

select first_name, last_name
from users inner join carts c on users.user_id = c.user_id left join orders o on c.cart_id = o.cart_id
where o.cart_id is null
limit 5;