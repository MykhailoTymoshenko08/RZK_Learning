# - Functions and Modules: *args, **kwards
# - Modular programming: how to split your code into multiply .py
# - OOP: include _ _init_ _, self, basic

# - JOINS: INNER, LEFT, RIGHT, FULL OUTHER
# - Subqueries: writing queries inside queries

import csv

with open("src/people-100.csv", 'r') as file:
    dataset = csv.DictReader(file)
    # dataset = csv.reader(file)
    i = 0
    for row in dataset:
        if i == 5:
            break
        print(row)
        i=i+1

with open("src/people-100.csv", "w") as file:
    writer = csv.DictWriter(file)
    writer.writerow(["Region", "Sales", "Bruh"])
    writer.writerow(["value1", "value2", "value3"])