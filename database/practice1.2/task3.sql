create or replace view customer_info as
    select id_customer, first_name, last_name, street, house_number, city, tel
    from customer join address using (id_address)
        join streets using (id_street)
        join houses using (id_house)
        join city using (id_city);

create or replace view car_info as
    select serial_number, brand, model, price, name, city
    from car join branch using (id_branch)
        join city using (id_city);

create materialized view orders_info as
    select first_name, last_name, tel, name, serial_number, brand, model, date_of_renting, period_of_renting
    from car_info join "car rental".public.orders using (serial_number)
        join customer_info using (id_customer);

select *
from customer_info;

select *
from car_info;

select *
from orders_info;

drop materialized view orders_info;
drop view customer_info;
drop view car_info;