SELECT
    region,
    SUM(revenue) AS total_revenue,
    COUNT(DISTINCT customer_id) AS customers
FROM sales_data
WHERE order_date >= '2024-01-01'
GROUP BY region
ORDER BY total_revenue DESC;
