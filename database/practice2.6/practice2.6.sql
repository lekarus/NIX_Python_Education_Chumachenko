create or replace view products_view as
    select product_title as "title", product_description as "descripion", in_stock as "in stock", price as "price"
    from products;
select *
from products_view;

create or replace view product_category_view as
    select product_title as "title", product_description as "descripion", in_stock as "in stock", price as "price",
           category_title as "category title", category_description as "category description"
    from products inner join categories using (category_id);
select *
from product_category_view;

create or replace view order_status_order_view as
    select shipping_total as "shipping total", total as "total", created_at as "created at", updated_at as "updated at",
           status_name as "status"
    from orders inner join order_status using(order_status_id);
select *
from order_status_order_view;

create materialized view order_products as
    select o.order_id as "order number", status_name as "status", o.total as "total", shipping_total as "shipping",
        created_at as "created", product_title as "product"
    from order_status inner join orders o using(order_status_id)
        inner join carts using(cart_id)
        inner join cart_product using(cart_id)
        inner join products using(product_id);

REFRESH MATERIALIZED VIEW order_products;
select *
from order_products;

drop view products_view;
drop view product_category_view;
drop view order_status_order_view;
drop materialized view order_products;