# - **Essence:** Protecting sensitive financial logic and automating overtime 
#   calculations for RZK Soft's services.
# - **TT:** Develop a ServiceInvoice class that uses private attributes to 
#   ensure data integrity and prevents manual "hacking" of hours or rates.
# - **Requirements:**
#     - **Data Protection:** Use a private attribute `__hours` (encapsulation). 
#       Use a "setter" method to update hours that rejects negative numbers.
#     - **Overtime Logic:** Calculate the total price based on the formula:
    
#     $Total = (RegularHours*Rate)+(OvertimeHours*rate*1.5)$
#     *(Overtime starts after 40 hours).*
    
#     - **Validation:** If someone tries to set `hours = -5`, the program 
#       must print an "Invalid Input" warning and keep the previous value.
#     - **Output:** A method `generate_invoice()` that prints a professional 
#       breakdown: Base pay, Overtime bonus, and Grand Total.

class ServiceInvoice():
    def __init__(self, rate):
        self.__hours = 0
        self.rate = rate

    def set_hours(self, hours):
        if hours >= 0:
            self.__hours = hours
        else:
            print("Invalid Input")

    def calculate_total(self):
        if self.__hours >= 40:
            return (40*self.rate)+(self.__hours-40)*self.rate*1.5
        else:
            return self.__hours*self.rate

    def generate_invoice(self):
        if self.__hours > 40:
            overtime = self.__hours-40
        else:
            overtime = 0

        total = self.calculate_total()
        
        print(f"{'Regular Hours:':<20}{self.__hours}")
        print(f"{'Overtime hours':<20}{overtime}")
        print(f"{'Base pay:':<20}{40*self.rate}")
        print(f"{'Overtime Bonus:':<20}{overtime*(self.rate * 1.5)}")
        print(f"{'Total:':<20}{total}")
        