create index idx_product_title
on products using btree (product_title);
drop index if exists idx_product_title;
explain select products.product_title
from products;

create index idx_carts_total
on carts using btree(total);
drop index if exists idx_carts_total;
explain select total
from carts
order by total;

create index idx_cp_products
on cart_product(product_id);
drop index if exists idx_cp_products;
explain select product_title
from products
where product_id = (select product_id
                    from cart_product
                    group by product_id
                    having count(*) = (select count(*)
                                        from cart_product
                                        group by product_id
                                        order by count(*) desc
                                        limit 1)
                    limit 1
    );