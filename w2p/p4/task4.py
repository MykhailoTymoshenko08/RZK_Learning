# - **Essence:** Using Classes to manage people in your firm
# - **TT:** Create an Employee class. Attribute name, role, 
#     salary, task_completed. Methods: add_task, 
#     calculate_bonus(bonus if tasks >5, 10% of salaty)
# - **Requirements:** create a list of 3-4 employee 
#     objects and trigger their methods in a loop.


class Employee:
    def __init__(itSelf, name, role, salary, task_completed):
        itSelf.name = name
        itSelf.role = role
        itSelf.salary = salary
        itSelf.task_completed = task_completed

    def __str__(itSelf):
        return f"Was created new employee {itSelf.name}"
    
    def add_task():
        pass

    def calculate_bonus():
        #bonus if tasks >5, 10% of salaty
        pass

MTymoshenko = Employee("Mykhailo Tymoshenko", "Founder, CEO & Lead Full-Stack/AI Engineer", 2000, 11)
MHaliapa = Employee("Mykhailo Haliapa", "Junior Developer (C/JavaScript) & COO", 1300, 7)
OTymoshenko = Employee("Olexii Tymoshenko", "Embedded / IoT Developer", 1200, 2)
VLavrientiev = Employee("Volodymyr Lavrientiev", "Lead Mobile Developer", 1200, 4)