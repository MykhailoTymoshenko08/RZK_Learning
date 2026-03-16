# - The modular CRM Engine
#     - **Essence:** Refactor “Mailing System” into a professional modular library
#     - **TT:** Split the code: main.py(execution), filters.py(logic for X amount/date), 
#         templates.py(message). Use **kwards to allow flexibility filtering 

import json
from filters import filter_cust
from templates import email_template
from datetime import date, timedelta

FILENAME = "data.json"

def send_email(input_dataset):
    print(f"Sending email to {input_dataset["name"]}")
    print(f"Last order date: {input_dataset["last_order_date"]}")
    print(email_template(input_dataset))

x = int(input("Enter X: "))

with open(FILENAME, "r") as f:
    dataset = json.load(f)
    dataset = dataset["customers"]

filtered = filter_cust(dataset, min_amount = x, max_date = "2026-02-16")

for cust in filtered:
    send_email(cust)


