# - Designing a "Digital Agency Management" scheme
# - **Essence:** Create a structure for managing the future company.
# - **TT:** You need to create tables: Clients, Projects, Employees, Tasks.
# - **Requirements:** Establish relationships (One Client — many Projects, 
# many Employees — one Project). Write an SQL query that will list all 
# projects for a specific client along with the names of the managers working on them.ʼ

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
POSTGRESQL_DB_PASSWORD = os.getenv("POSTGRESQL_DB_PASSWORD")

#db config
conn = psycopg2.connect(
    host = "localhost",
    database = "project3",
    user = "tymoshenkomykhailo",
    password=POSTGRESQL_DB_PASSWORD
)
cursor = conn.cursor()

def creating_tables_if_not_exist():
    query = '''
    CREATE TABLE IF NOT EXISTS Clients (
        client_id SERIAL PRIMARY KEY,
        client_name VARCHAR(255) NOT NULL
    );
    CREATE TABLE IF NOT EXISTS Projects (
        project_id SERIAL PRIMARY KEY,
        project_name VARCHAR(255) NOT NULL,
        client_id INT NOT NULL REFERENCES Clients(client_id)
    );
    CREATE TABLE IF NOT EXISTS Employees (
        employee_id SERIAL PRIMARY KEY,
        employee_name VARCHAR(255) NOT NULL,
        project_id INT NOT NULL REFERENCES Projects(project_id)
    );
    CREATE TABLE IF NOT EXISTS Tasks (
        task_id SERIAL PRIMARY KEY,
        task_name VARCHAR(255) NOT NULL,
        project_id INT NOT NULL REFERENCES Projects(project_id),
        employee_id INT NOT NULL REFERENCES Employees(employee_id)
    );
'''
    cursor.execute(query)
    conn.commit()
    print("Tables were created")

def insert_info():
    query = '''
    INSERT INTO Clients (client_name) VALUES
    ('Google'),
    ('Amazon'),
    ('Netflix');
    INSERT INTO Projects (project_name, client_id) VALUES
    ('Website', 1),             -- Google
    ('Mobile App', 1),          -- Google
    ('Cloud System', 2),        -- Amazon
    ('Streaming Platform', 3);  -- Netflix
    INSERT INTO Employees (employee_name, project_id) VALUES
    ('Alice', 1),   -- Website
    ('Bob', 1),     -- Website
    ('Charlie', 2), -- Mobile App
    ('David', 3);   -- Cloud System
    INSERT INTO Tasks (task_name, project_id, employee_id) VALUES
    ('Design Homepage', 1, 1),   -- Alice
    ('Build Backend', 1, 2),     -- Bob
    ('Create Mobile UI', 2, 3),  -- Charlie
    ('Cloud Infrastructure', 3, 4), -- David
    ('Video Player', 4, 2);      -- Bob
'''
    cursor.execute(query)
    conn.commit()
    print("Info were addes(inserted)")

def delete_tables():
    query = '''
    drop table if exists Tasks;
    drop table if exists Employees;
    drop table if exists Projects;
    drop table if exists Clients;
'''
    cursor.execute(query)
    conn.commit()
    print("Tables were deleted")

def get_info(client_ids):
    query = '''
    SELECT
        c.client_name,
        p.project_name,
        e.employee_name
    FROM Clients c
    JOIN Projects p ON c.client_id = p.client_id
    JOIN Tasks t ON p.project_id = t.project_id
    JOIN Employees e ON t.employee_id = e.employee_id
    WHERE c.client_id = %s
'''
    cursor.execute(query, (client_ids,))
    return cursor.fetchall()


# creating_tables_if_not_exist()
# insert_info()

client_id = int(input("Write client's id to see info: "))
if isinstance(client_id, int):
    print(get_info(client_id))
else:
    print("That isn't a number!!!!!!!")

# delete_tables()

#closing I/O
cursor.close()
conn.close()
print("Posgre Sever closed")