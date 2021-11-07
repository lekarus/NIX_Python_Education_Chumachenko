create or replace procedure set_2x_price()
    language sql as $$
    update car set price = price * 2;
    $$;

create or replace procedure update_last_name()
    language sql as $$
    update customer c1 set last_name = 'second name ' || (select c2.id_customer from customer c2
                                                            where c1.id_customer = c2.id_customer);
    $$;

begin;
select * from car;
call set_2x_price();
select * from car;
call update_last_name();
select * from customer;
rollback;
