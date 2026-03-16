# - **Essence:** Automating the "boring" stuff. Moving data from marketing 
#     spreadsheets (CSV) into your professional PostgreSQL database
# - **TT:** Write a Python script that reads a list of "Potential Leads" 
#     from a .csv file and saves them into your clients table in Postgres
# - **Requirements:**
    # - **Input File:** Create a `leads.csv` with columns: `name`, `email`, `estimated_budget`.
    # - **CSV Processing:** Use the built-in `csv` module to read the file row by row.
    # - **Data Cleaning:** If a row has an empty email or the budget is 
    #     not a number, skip that row and print a "Corrupted Data" warning.
    # - **Database Integration:** For every valid row, execute an `INSERT` 
    #     statement into your PostgreSQL database.
    # - **Reporting:** At the end of the script, output: *"Successfully migrated "
    # "   [X] leads to the database. [Y] rows were skipped due to errors."*

import csv
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
POSTGRESQL_DB_PASSWORD = os.getenv("POSTGRESQL_DB_PASSWORD")

conn = psycopg2.connect(
    host = "localhost",
    database = "w2p_t1",
    user = "tymoshenkomykhailo",
    password=POSTGRESQL_DB_PASSWORD
)
cursor = conn.cursor()
print("Database was connected")

def createTableIfNotExists():
    query = '''
        CREATE TABLE IF NOT EXISTS Leads(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            estimated_budget INT 
        );
    '''
    cursor.execute(query)
    conn.commit()
    print("Table was created")

createTableIfNotExists()

try:
    with open("src/leads.csv", "r") as file:
        skippedCount = 0
        completedCount = 0
        dataset = csv.DictReader(file)
        for row in dataset:
            name = row["name"]
            email = row["email"]
            estimated_budget = int(row["estimated_budget"])

            if email is None or not isinstance(estimated_budget, int):
                print("Corrupted Data")
                skippedCount = skippedCount + 1
                continue
                
            cursor.execute(
                "INSERT INTO leads (name, email, estimated_budget) VALUES (%s, %s, %s);",
                (name, email, estimated_budget)
            )
            conn.commit()
            completedCount = completedCount + 1
        print(f"Successfully migrated {completedCount} leads to the database. {skippedCount} rows were skipped due to errors.")
except:
    print("File was not found")


cursor.close()
conn.close()
print("Postgre Sever closed")