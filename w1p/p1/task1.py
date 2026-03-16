import json
import os

# Business process logging and analysis system (CLI)

# Essence: A program that simulates working time tracking.

# TT: The user enters the task name and the time spent. 
# The data is stored in JSON. The program should be able 
# to output a report: total time per day, longest task, 
# average task duration.

FILENAME = "data.json"

def show_menu():
    print('='*50)
    print("Write 1 to show task's list") #done
    print("Write 2 to add a new task")
    print("Write 3 to get task's report")
    print("Write 0 to exit") #done
    print('='*50)

def show_task_list():
    file_opening_var = open(FILENAME, 'r')
    file_reading_mode = file_opening_var.read()
    dataset = json.loads(file_reading_mode)
    for i in range(len(dataset)):
        print(f"Task id: {i}")
        print(f"Task name: {dataset[i]['task_name']}")
        print(f"Time spent: {dataset[i]['task_time_spent']}\n")
    file_opening_var.close()

def get_report():
    file_opening_var = open(FILENAME, 'r')
    file_reading_mode = file_opening_var.read()
    dataset = json.loads(file_reading_mode)
    total_time = 0
    longest_task_id = 0
    for i in range(len(dataset)):
        total_time += dataset[i]["task_time_spent"]
        if dataset[longest_task_id]["task_time_spent"] < dataset[i]["task_time_spent"]:
            longest_task_id = i

    avarage_time_duration = total_time/(i+1)

    print(f"The total time per day: {total_time}")
    print(f"The longest tast: {dataset[longest_task_id]["task_name"]}, {dataset[longest_task_id]["task_time_spent"]} minutes")
    print(f"Avarage time duration: {avarage_time_duration} minutes")
    file_opening_var.close()

def save_new_dataset(dataset):
    file_opening_var = open(FILENAME, 'w')
    json.dump(dataset, file_opening_var, indent=4)
    file_opening_var.close()


def add_new_task():
    file_opening_var = open(FILENAME, 'r')
    file_reading_mode = file_opening_var.read()
    dataset = json.loads(file_reading_mode)

    new_task_name = input("Enter the new task name:")
    new_task_time_spent = int(input("Enter the time spent: "))

    new_task = {
        "task_name": new_task_name,
        "task_time_spent": new_task_time_spent
    }
    dataset.append(new_task)
    file_opening_var.close()
    save_new_dataset(dataset)



command_input = 1
while(command_input !=0):
    print('\n')
    show_menu()
    command_input = int(input("Write command number: "))
    print('\n')
    match command_input:
        case 0: 
            print("Ending program")
            exit()
        case 1:
            show_task_list()
        case 2:
            add_new_task()
        case 3:
            get_report()
        case _:
            print("Invalid value")
