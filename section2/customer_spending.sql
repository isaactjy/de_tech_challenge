-- I want to know the list of our customers and their spending.

SELECT 
	a.customer_id, 
	CONCAT(b.customer_firstname,' ',b.customer_lastname) AS customer_name,
	SUM(c.price) AS spending
FROM dealership.transactions a
INNER JOIN dealership.customers b
ON a.customer_id = b.customer_id
LEFT JOIN dealership.cars c
ON a.car_id = c.car_id
GROUP BY 1,2