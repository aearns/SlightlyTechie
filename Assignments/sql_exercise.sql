
CREATE TABLE products(
    id SERIAL PRIMARY KEY NOT NULL, 
    product_name VARCHAR(50) NOT NULL, 
    category VARCHAR(50), 
    price NUMERIC NOT NULL
);

INSERT INTO products(product_name, category, price) 
VALUES
    ("Blood Pressure Monitor", "Medical Devices", 50.00),
    ("Fitness Tracker", "Wearables", 120.00),
    ("Thermometer (Digital)", 'Medical Devices', 15.00),
    ("Organic Multivitamins", 'Supplements', 25.00),
    ("First Aid Kit", "Emergency Supplies",	35.00);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    CONSTRAINT fk_product_sales FOREIGN KEY (product_id) REFERENCES product(id),
    product_id VARCHAR(10) UNIQUE,
    quantity_sold INT NOT NULL,
    sale_date DATE NOT NULL,
    total_price NUMERIC NOT NULL  
);

INSERT INTO sales (id, product_id, quantity_sold, sale_date, total_price) 
VALUES
    (1, 1, 2, '2024-08-05', 199.98),
    (2, 3, 1, '2024-08-06', 289.99),
    (3, 2, 3, '2024-08-07', 29.99),
    (4, 5, 2, '2024-08-08', 89.98),
    (5, 4, 1, '2024-08-09', 729.99);

SELECT * FROM product

SELECT product_name, price FROM product

SELECT * FROM sales LIMIT 2

SELECT * FROM sales WHERE total_price > 100

SELECT category, COUNT(*) AS product_count
    FROM products
    GROUP BY category
    HAVING COUNT(*) > 1;

SELECT COUNT(*) AS total_product FROM product

SELECT SUM(total_price) AS total_sales from sales

SELECT AVG(price) AS average_price FROM product 

