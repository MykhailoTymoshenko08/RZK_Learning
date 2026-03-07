-- Warehouse accounting with analytics
-- **Essence:** Inventory accounting with analytics (Advanced queries)
-- **TT:** Create a Products and Sales table.
-- **Requirements:** Write an SQL query (using GROUP BY and JOIN) 
-- that will show: the TOP 3 most profitable products, total revenue 
-- for the last week, and a list of products with less than 5 units in stock.

CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE Sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES Products(product_id),
    quantity INT NOT NULL,
    sale_date DATE NOT NULL
);

INSERT INTO Products (product_name, price, stock) VALUES
('Laptop', 1200.00, 10),
('Mouse', 25.00, 50),
('Keyboard', 70.00, 30),
('Monitor', 300.00, 7),
('Headphones', 150.00, 3),
('USB Cable', 10.00, 100),
('Webcam', 90.00, 4);


INSERT INTO Sales (product_id, quantity, sale_date) VALUES
(1, 2, CURRENT_DATE - INTERVAL '2 days'),
(1, 1, CURRENT_DATE - INTERVAL '6 days'),
(2, 10, CURRENT_DATE - INTERVAL '1 day'),
(3, 5, CURRENT_DATE - INTERVAL '3 days'),
(4, 2, CURRENT_DATE - INTERVAL '8 days'),
(5, 1, CURRENT_DATE - INTERVAL '2 days'),
(6, 20, CURRENT_DATE - INTERVAL '4 days'),
(7, 2, CURRENT_DATE - INTERVAL '5 days'),
(3, 2, CURRENT_DATE - INTERVAL '1 day'),
(2, 5, CURRENT_DATE - INTERVAL '6 days');