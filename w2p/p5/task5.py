# - **Essence:** A CLI app that actually saves data to PostgreSQL instead of JSON
# - **TT:** Python script that asks for a task name and status.
# - **Requirements:** It must INSERT the task into a Postgres table. 
#     Another command must SELECT and display all unfinished tasks.


import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DBPASS = os.getenv("DBPASS")

conn = psycopg2.connect(
    host = "localhost",
    database = "task1_ench",
    user = "tymoshenkomykhailo",
    password = DBPASS
)
cursor = conn.cursor()


class Task():
    def __init__(self, name, status):
        self.name = name
        self.status = status
        print("Task was created")

    def displayAllUnCompletedTasks():
        query = '''
            SELECT name
            FROM tasks
            WHERE status = 'unCompleted'
        '''
        cursor.execute(query)
        col = cursor.fetchall()
        for name in col:
            print(name)

    def addNewTask():
        newTaskName = input("Write task name: ")
        newTaskStatus = input("Write task status(Completed, unCompleted): ")
        query = '''
            INSERT INTO tasks (name, status)
            VALUES(%s,%s)
        '''
        cursor.execute(query, (newTaskName, newTaskStatus))
        conn.commit()

def printMenu():
    print('='*20)
    print("Write 1 to display all uncompleted tasks")
    print("Write 2 to add new task")
    print("Write 0 to exit")

command = 1
while command != 0:
    print("\n\n")
    printMenu()
    command = int(input("Write your choise: "))
    print("\n")
    match command:
        case 0: break
        case 1: Task.displayAllUnCompletedTasks()
        case 2: Task.addNewTask()


cursor.close()
conn.close()
print("Posgre server was closed")