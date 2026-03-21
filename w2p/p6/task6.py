# - **Essence:** Building on your "Warehouse" project
# - **TT:** Use a Subquery to find all products whose stock 
#     is *below the average* stock of all products in the warehouse
# - **Requirements:** Output the Product Name, Current Stock, 
#     and the "Gap" (Average - Current)

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

query = '''
    SELECT product_name, stock, 
        ROUND((SELECT AVG(stock)
        FROM products)
        - stock, 2) AS Gap
    FROM products
    WHERE stock < (SELECT AVG(stock) FROM products);
'''
cursor.execute(query)
result = cursor.fetchall()
print(f"{'Product Name':<20}{'Curr':<10}{'Stock Gap':<10}")
print('-'*50)
for row in result:
    print(f"{row[0]:<20}{row[1]:<10}{row[2]:<10}")



cursor.close()
conn.close()