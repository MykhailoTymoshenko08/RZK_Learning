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