create or replace function select_cars(tmp_price int)
    returns table ("car serial number" int, "car brand" varchar, "car model" varchar)
    language 'plpgsql'
    as $$
    begin
        return query select serial_number, brand, model
        from car where price > tmp_price::money;
    end;
    $$;

create or replace function count_orders(tmp_date date)
    returns int
    language 'plpgsql'
    as $$
    declare
        curs1 cursor for select * from "car rental".public.orders where date_of_renting < tmp_date;
        row orders%rowtype;
        counter int := 0;
    begin
        for row in curs1
        loop
            counter := counter + 1;
        end loop;
        return counter;
    end;
    $$;

drop function count_orders(tmp_date date);
drop function select_cars(tmp_price int);

select *
from select_cars(100);

select *
from count_orders('12/12/2014');