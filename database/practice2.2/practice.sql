select *
from users;

select *
from products;

select *
from order_status;

select *
from order_status inner join orders o on order_status.order_status_id = o.order_status_id
where order_status.status_name = 'Finished';

select *
from products
where price between 80 and 150;

select *
from products
where price > 80 and price <= 150;

select *
from orders
where created_at > '01/10/2020';

select *
from orders
where created_at > '01/01/2020' and created_at < '07/01/2020';

select *
from products inner join categories c on c.category_id = products.category_id
where c.category_title = 'Category 7' or c.category_title = 'Category 8' or c.category_title = 'Category 11';

select *
from orders inner join order_status os on os.order_status_id = orders.order_status_id
where orders.created_at <= '12/31/2020' and os.status_name != 'Finished';

select *
from carts inner join orders o on carts.cart_id = o.cart_id
    inner join order_status os on os.order_status_id = o.order_status_id
where os.status_name != 'Finished';

select avg(carts.total)
from carts inner join orders o on carts.cart_id = o.cart_id
    inner join order_status os on os.order_status_id = o.order_status_id
where os.status_name = 'Finished';

select max(carts.total)
from carts inner join orders o on carts.cart_id = o.cart_id
    inner join order_status os on os.order_status_id = o.order_status_id
where o.created_at >= '7/01/2020' and o.created_at < '10.01.2020';
