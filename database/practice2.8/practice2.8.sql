select category_title, product_title, price, avg(price) over(partition by category_id),
       price - avg(price) over(partition by category_id) as diff
from categories join products using(category_id)
order by category_title;


CREATE OR REPLACE FUNCTION func_insert_city() RETURNS TRIGGER AS $$
BEGIN
    if new.city not like '%city%' then new.city = 'city 17';
    end if;
    return new;
END
$$ LANGUAGE 'plpgsql';
create trigger insert_city before insert on potential_customers
    for each row execute procedure func_insert_city();
drop trigger insert_city on potential_customers;
drop function func_insert_city() cascade;

begin;
insert into potential_customers values(default, 'email10@ail.com', 'name10', 'surname10', 'second_name10', 'city 10');
select * from potential_customers;
rollback;

CREATE OR REPLACE FUNCTION func_update_total() RETURNS TRIGGER AS $$
BEGIN
    if new.total < old.total then
        return null;
    end if;
    return new;
END
$$ LANGUAGE 'plpgsql';
create trigger update_total before update on orders
    for each row execute procedure func_update_total();
drop trigger update_total on orders;
drop function func_update_total() cascade;

begin;
update orders set total = 0 where order_id = 1;
select * from orders where order_id = 1;
rollback;