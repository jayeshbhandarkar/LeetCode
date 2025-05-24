select customer_id from Customer GROUP BY customer_id
HAVING count(distinct product_key) = (select count(product_key) from Product);
