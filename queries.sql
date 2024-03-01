-- QUERY 1 ----------------------------------------------------------------------------
SELECT
    order_id,
    ROUND(julianday(order_delivered_customer_date) - julianday(order_estimated_delivery_date), 1) AS delay_days,
    order_purchase_timestamp
FROM 
    orders
WHERE
    order_status <> 'canceled'
    AND order_status = 'delivered'
    AND order_delivered_customer_date IS NOT NULL
    AND delay_days >= 3
    AND julianday('2018-10-17') - julianday(order_purchase_timestamp) <= 90
ORDER BY
    delay_days DESC;

-- QUERY 2 ----------------------------------------------------------------------------
SELECT
    seller_id,
    ROUND(SUM(price), 2) AS total_income
FROM
    order_items
GROUP BY
    seller_id
HAVING
    total_income > 100000
ORDER BY
    total_income DESC;

-- QUERY 3 ----------------------------------------------------------------------------
SELECT
    order_items.seller_id,
    MIN(orders.order_purchase_timestamp) AS first_order_date,
    COUNT(order_items.order_id) AS total_orders
FROM
    order_items
JOIN
    sellers ON order_items.seller_id = sellers.seller_id
JOIN
    orders ON orders.order_id = order_items.order_id
GROUP BY
    order_items.seller_id
HAVING
    julianday('2018-10-17') - julianday(first_order_date) <= 90
    AND total_orders >= 30
ORDER BY
    total_orders DESC;

-- QUERY 4 ----------------------------------------------------------------------------
SELECT
    sellers.seller_zip_code_prefix AS post_code,
    ROUND(AVG(order_reviews.review_score), 2) AS avg_score,
    COUNT(order_items.order_id) AS total_orders
FROM
    sellers
JOIN
    order_items ON sellers.seller_id = order_items.seller_id
JOIN
    order_reviews ON order_items.order_id = order_reviews.order_id
JOIN
    orders ON orders.order_id = order_items.order_id
WHERE
    julianday('2018-10-17') - julianday(order_purchase_timestamp) < 365
GROUP BY
    sellers.seller_zip_code_prefix
HAVING
    total_orders >= 30
ORDER BY
    avg_score ASC
LIMIT 5;
