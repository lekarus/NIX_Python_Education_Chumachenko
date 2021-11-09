create function func_delete_car() returns trigger as $$
begin
    delete from "car rental".public.orders o where o.serial_number = old.serial_number;
    return null;
end;
$$ language plpgsql;

create function func_delete_orders() returns trigger as $$
    declare
        counter int;
    begin
        select count(*) from "car rental".public.orders where id_customer = old.id_customer into counter;
        if counter = 0 then
            delete from customer where id_customer = old.id_customer;
        end if;
        return null;
        end;
$$ language plpgsql;

create trigger delete_car before delete on car
    for each row execute procedure func_delete_car();
create trigger delete_order after delete on "car rental".public.orders
    for each row execute procedure func_delete_orders();


drop function func_delete_car();
drop function func_delete_orders();
drop trigger delete_car on car;
drop trigger delete_order on "car rental".public.orders;

begin;
select * from "car rental".public.orders where serial_number = 46;
delete from car where serial_number = 46;
delete from "car rental".public.orders where id_customer = 8;
select * from customer where id_customer = 8;
rollback;
