-- I want to find out the top 3 car manufacturers that customers bought by sales 
-- (quantity) and the sales number for it in the current month.

WITH current_month_sales AS ( 
	SELECT 
	a.transaction_id,
	b.manufacturer
	FROM dealership.transactions a
	INNER JOIN dealership.cars b
	ON a.car_id = b.car_id
	COUNT(
	WHERE extract(YEAR FROM a.transaction_date) = extract(YEAR FROM now())
		and extract(MONTH FROM a.transaction_date) = extract(MONTH FROM now())
)
SELECT 
manufacturer,
COUNT(transaction_id) AS sales
FROM current_month_sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 3