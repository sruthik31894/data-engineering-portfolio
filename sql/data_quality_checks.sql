SELECT COUNT(*) AS null_customer_ids
FROM sales_data
WHERE customer_id IS NULL;

SELECT order_id, COUNT(*)
FROM sales_data
GROUP BY order_id
HAVING COUNT(*) > 1;
