
CREATE TABLE products(
    id SERIAL PRIMARY KEY NOT NULL, 
    product_name VARCHAR(50) NOT NULL, 
    category VARCHAR(50), 
    price FLOAT NOT NULL
);

INSERT INTO products(product_name, category, price) 
VALUES
    ("Blood Pressure Monitor", "Medical Devices", 50.00),
    ("Fitness Tracker", "Wearables", 120.00),
    ("Thermometer (Digital)", 'Medical Devices', 15.00),
    ("Organic Multivitamins", 'Supplements', 25.00),
    ("First Aid Kit", "Emergency Supplies",	35.00);

CREATE TABLE Sales (
    id SERIAL PRIMARY KEY,
    product_id VARCHAR(10) UNIQUE,
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10,20),  
);

