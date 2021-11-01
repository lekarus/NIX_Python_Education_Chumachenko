begin;
    savepoint work_potential_customers;
    insert into potential_customers values(default, 'email10@mail.com', 'name10', 'surname10', 'second_name10', 'ciy10');
    update potential_customers set name = 'name111' where city = 'city17';
    delete from potential_customers where city = 'city1';
    select *
    from potential_customers;
    rollback to savepoint work_potential_customers;
commit;

begin;
    savepoint work_products;
    insert into products values((select max(product_id)+1 from products), 'product0', 'Product description 0', 25, 15.2, 'Product-0', 1);
    update products set price = price / 2;
    delete from products where product_id not in (select product_id from cart_product);
    select *
    from products
    order by product_id;
    rollback to savepoint work_products;
commit;

begin;
    savepoint work_categories;
    insert into categories values((select max(categories.category_id)+1 from categories), 'category 0', 'category 0 description');
    update categories set category_description = 'not used' where category_id not in (select distinct category_id from products);
    delete from categories where category_description = 'not used';
    select *
    from categories;
    rollback to savepoint work_categories;
commit;