create index customer_idx_first_name on customer using btree (first_name);
create index car_idx_serial_number on car using btree (serial_number);
create index order_idx_customer on "car rental".public.orders using btree (id_customer);
drop index customer_idx_first_name;
drop index car_idx_serial_number;
drop index order_idx_customer;

explain select first_name, last_name, city.city, tel
from customer join city using (id_city)
where first_name = 'first name 1';

explain select serial_number
from car join orders using (serial_number)
where price > 100::money;

explain select first_name, last_name
from city join customer using (id_city)
    left join "car rental".public.orders using (id_customer)
where city = 'city 10';