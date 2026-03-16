# - Warehouse accounting with analytics
# - **Essence:** Inventory accounting with analytics (Advanced queries)
# - **TT:** Create a Products and Sales table.
# - **Requirements:** Write an SQL query (using GROUP BY and JOIN) 
# that will show: the TOP 3 most profitable products, total revenue 
# for the last week, and a list of products with less than 5 units in stock.

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
POSTGRESQL_DB_PASSWORD = os.getenv("POSTGRESQL_DB_PASSWORD")

conn = psycopg2.connect(
    host = "localhost",
    database = "proj5",
    user = "tymoshenkomykhailo",
    password = POSTGRESQL_DB_PASSWORD
)
cursor = conn.cursor()



def creating_tables_if_not_exist():
    query = '''
    CREATE TABLE IF NOT EXISTS Products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        stock INT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Sales (
        sale_id SERIAL PRIMARY KEY,
        product_id INT NOT NULL REFERENCES Products(product_id),
        quantity INT NOT NULL,
        sale_date DATE NOT NULL
    );
'''
    cursor.execute(query)
    conn.commit()
    print("Tables were created")

def insert_info():
    query = '''
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
'''
    cursor.execute(query)
    conn.commit()
    print("Info were addes(inserted)")

def delete_tables():
    query = '''
    drop table if exists Products;
    drop table if exists Sales;
'''
    cursor.execute(query)
    conn.commit()
    print("Tables were deleted")

# creating_tables_if_not_exist()
# insert_info()
# delete_tables()


def top_profitable_products():
    query = '''
    SELECT p.product_name, SUM(s.quantity * p.price) AS total_revenue
    FROM Sales s
    JOIN Products p ON s.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_revenue DESC
    LIMIT 3;
'''
    cursor.execute(query)
    result = cursor.fetchall()
    print("Top 3 most profitable products:")
    for row in result: 
        print(f"{row[0]}: ${row[1]}")

def total_revenue_last_week():
    query = '''
    SELECT SUM(s.quantity * p.price) AS total_revenue
    FROM Sales s
    JOIN Products p ON s.product_id = p.product_id
    WHERE s.sale_date >= CURRENT_DATE - INTERVAL '7 days';
'''
    cursor.execute(query)
    result = cursor.fetchone()
    print(f"\nTotal revenue for the last week: ${result[0]}")

def products_low_stock():
    query = '''
    SELECT product_name, stock
    FROM Products
    WHERE stock < 5;
'''
    cursor.execute(query)
    result = cursor.fetchall()
    print("\nProducts with less than 5 units in stock:")
    for row in result:
        print(f"{row[0]}: {row[1]} units")

top_profitable_products()
total_revenue_last_week()
products_low_stock()


cursor.close()
conn.close()
