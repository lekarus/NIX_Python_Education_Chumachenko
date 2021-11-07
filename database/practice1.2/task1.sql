create database "car rental";

create schema public;

create table city(
    id_city serial primary key,
    city varchar(255) not null
);

create table streets(
    id_street serial primary key,
    street varchar(255) not null
);

create table houses(
    id_house serial primary key,
    house_number varchar(255) not null
);

create table address(
    id_address serial primary key,
    id_street int not null,
    id_house int not null,
    foreign key (id_street) references streets (id_street),
    foreign key (id_house) references houses (id_house)
);

create table branch(
    id_branch serial primary key,
    id_city int not null,
    id_address int not null,
    name varchar(255) not null,
    tel varchar(10) not null,
    foreign key (id_address) references address (id_address),
    foreign key (id_city) references city (id_city)
);

create table customer(
    id_customer serial primary key,
    id_city int not null,
    id_address int not null,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    tel varchar(10) not null,
    foreign key (id_address) references address (id_address),
    foreign key (id_city) references city (id_city)
);

create table car(
  serial_number serial primary key,
  id_branch int not null,
  brand varchar(255) not null,
  model varchar(255) not null,
  price money not null,
  foreign key (id_branch) references branch (id_branch)
);

create table orders(
  id_order serial primary key,
  id_customer int not null,
  id_car int not null,
  date_of_renting date not null,
  period_of_renting int,
  foreign key (id_car) references car (serial_number),
  foreign key (id_customer) references customer (id_customer)
);

create sequence seq1 start 1;
create sequence seq2 start 1;
create sequence seq3 start 1;

create or replace procedure insert_city(number int) language plpgsql as $$
    declare
        i int;
    begin
        alter sequence seq1 restart;
        for i in 1..number
        loop
            insert into city values(default, 'city ' || nextval('seq1'));
        end loop;
    end;
$$;

create or replace procedure insert_houses(number int) language plpgsql as $$
    declare
        i int;
    begin
        alter sequence seq1 restart;
        for i in 1..number
        loop
            insert into houses values(default, nextval('seq1'));
        end loop;
    end;
$$;

create or replace procedure insert_streets(number int) language plpgsql as $$
    declare
        i int;
    begin
        alter sequence seq1 restart;
        for i in 1..number
        loop
            insert into streets values(default, 'street ' || nextval('seq1'));
        end loop;
    end;
$$;

create or replace procedure insert_address(number int) language plpgsql as $$
    declare
        i int;
    begin
        for i in 1..number
        loop
            insert into address values(default, (random()*(200-1)+1)::int, (random()*(300)-1+1)::int);
        end loop;
    end;
$$;

create or replace procedure insert_branch(number int) language plpgsql as $$
    declare
        i int;
    begin
        alter sequence seq1 restart;
        alter sequence seq2 restart;
        for i in 1..number
        loop
            insert into branch values(default, (random()*(20-1)+1)::int, (random()*(250)-1+1)::int,
                                      'name '::text || nextval('seq1'), 'tel '::text || nextval('seq2'));
        end loop;
    end;
$$;

create or replace procedure insert_customer(number int) language plpgsql as $$
    declare
        i int;
    begin
        alter sequence seq1 restart;
        alter sequence seq2 restart;
        alter sequence seq3 restart;
        for i in 1..number
        loop
            insert into customer values(default, (random()*(20-1)+1)::int, (random()*(250)-1+1)::int,
                                      'first name '::text || nextval('seq1'), 'last name '::text || nextval('seq2'),
                                      'tel '::text || nextval('seq3'));
        end loop;
    end;
$$;

create or replace procedure insert_car(number int) language plpgsql as $$
    declare
        i int;
    begin
        alter sequence seq1 restart;
        alter sequence seq2 restart;
        for i in 1..number
        loop
            insert into car values(default, (random()*(100-1)+1)::int,
                                      'brand '::text || nextval('seq1'), 'model '::text || nextval('seq2'),
                                      random()*(300)::money);
        end loop;
    end;
$$;

create or replace procedure insert_orders(number int) language plpgsql as $$
    declare
        i int;
    begin
        for i in 1..number
        loop
            insert into orders values(default, (random()*(200-1)+1)::int, (random()*(100-1)+1)::int,
                                      (to_timestamp(1388534400+random()*247190399))::date, (random()*(30-1)+1)::int);
        end loop;
    end;
$$;

call insert_city(20);
call insert_houses(300);
call insert_streets(200);
call insert_address(250);
call insert_branch(100);
call insert_customer(200);
call insert_car(100);
call insert_orders(300);

drop sequence seq1;
drop sequence seq2;
drop sequence seq3;
drop procedure insert_houses(number int);
drop procedure insert_city(number int);
drop procedure insert_streets(number int);
drop procedure insert_address(number int);
drop procedure insert_branch(number int);
drop procedure insert_customer(number int);
drop procedure insert_car(number int);
drop procedure insert_orders(number int);
