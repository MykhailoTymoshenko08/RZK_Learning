# - Mailing automation system (Logic engine)
# - **Essence:** Creating a logical "engine" for filtering customers.
# - **TT:** We have a list of customers (name, subscription status, 
# last order date, amount spent). The program should generate personalized 
# text messages only for those who spent more than X amount AND haven't 
#     ordered anything for more than a month.

import json


FILENAME = "customers_data.json"

def send_email(input_dataset):
    print(f"Sending email to {input_dataset["name"]}")
    print(f"Last order date: {input_dataset["last_order_date"]}")

x = int(input("Enter X: "))

with open(FILENAME, "r") as f:
    dataset = json.load(f)
    dataset = dataset["customers"]

for i in range(len(dataset)):
    if dataset[i]["amount_spent"] > x and dataset[i]["last_order_date"] > "2026-02-07":
        send_email(dataset[i])

