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
    
    def add_task(itSelf):
        itSelf.task_completed = itSelf.task_completed + 1
        print(f"Task completed: {itSelf.task_completed}")

    def calculate_bonus(itSelf):
        #bonus if tasks >5, 10% of salaty
        if itSelf.task_completed > 5:
            bonus = itSelf.salary*0.1
            print(f"Employee get bonus, bonus: {bonus}")
        else:
            print("Employee doesn't get bonus")

MTymoshenko = Employee("Mykhailo Tymoshenko", "Founder, CEO & Lead Full-Stack/AI Engineer", 2000, 11)
MHaliapa = Employee("Mykhailo Haliapa", "Junior Developer (C/JavaScript) & COO", 1300, 7)
OTymoshenko = Employee("Olexii Tymoshenko", "Embedded / IoT Developer", 1200, 2)
VLavrientiev = Employee("Volodymyr Lavrientiev", "Lead Mobile Developer", 1200, 4)

MTymoshenko.add_task()
MHaliapa.calculate_bonus()
OTymoshenko.calculate_bonus()
VLavrientiev.calculate_bonus()