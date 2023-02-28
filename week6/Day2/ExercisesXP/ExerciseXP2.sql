-- select * from customer;

-- select first_name || ' ' || last_name as full_name from customer;

-- select distinct create_date from customer;

-- select * from customer
-- order by first_name DESC;


-- select film_ID, title, description, release_year, rental_rate from film
-- order by rental_rate;

-- select first_name, last_name, district from customer
-- join address
-- on
-- customer.address_id = address.address_id 
-- where district = 'Texas';

-- select * from film where film_id =15 or film_id=150;

-- select * from film where title = 'fight club';

-- select  film_ID, title, description, length, rental_rate from film where title like 'fi________%';

-- select * from film order by rental_rate limit 10;

-- select * from film order by rental_rate asc offset 10 fetch first 10 row only;

-- select customer.customer_id , customer.first_name, customer.last_name, payment.payment_date, payment.amount
-- from customer
-- join payment
-- on customer.customer_id = payment.customer_id
-- order by customer_id;

-- select * from film where film_id not in(select film_id from inventory);

-- select city.city, country.country
-- from city
-- join country
-- on country.country_id = city.country_id;