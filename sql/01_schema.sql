-- Table to store cleaned sales data
CREATE TABLE fact_sales (
    order_id INT,
    order_date DATE,
    customer_id VARCHAR(50),
    region VARCHAR(50),
    product_category VARCHAR(50),
    product_name VARCHAR(100),
    quantity INT,
    unit_price DECIMAL(10,2),
    discount DECIMAL(4,2),
    sales_amount DECIMAL(12,2),
    cost_amount DECIMAL(12,2),
    profit_amount DECIMAL(12,2),
    order_month VARCHAR(7),
    order_year INT,
    profit_margin DECIMAL(6,4)
);