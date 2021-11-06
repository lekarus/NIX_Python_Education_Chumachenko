create function set_shipping(input_city varchar(32)) returns void as $$
        begin
                update orders set shipping_total = 0
                where order_id in (select order_id
                                    from orders join carts using(cart_id) join users using(user_id)
                                    where users.city = input_city);
                if not found then
                    raise 'not found';
                end if;
        end;
$$ language plpgsql;
drop function set_shipping(input_city varchar);

begin;
select set_shipping('city 1');
select shipping_total
from orders join carts using(cart_id) join users using(user_id)
where city = 'city 1';
rollback;

create or replace procedure update_order_status(input_id integer) language plpgsql as $$
begin
update orders set order_status_id = 5 where order_id = input_id;
end $$;
drop procedure update_order_status(input_id integer);

begin;
call update_order_status(2);
select order_status_id
    from orders
        where order_id = 2;
rollback;


create or replace procedure set_2x_total(input_control decimal) language plpgsql as $$
declare
    r orders%rowtype;
begin
    for r in select * from orders
    loop
        if r.total < input_control then
            update orders set total = total * 2 where order_id = r.order_id;
        end if;
    end loop;
end $$;
drop procedure set_2x_total(input_control decimal);

begin;
call set_2x_total(500);
select order_id, total
from orders
where order_id = 1;
rollback;