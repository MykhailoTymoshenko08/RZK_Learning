# - **Essence:** Building a scalable structure to 
#   manage the diverse client base of RZK Soft
# - **TT:** Create a base class Client and specialized 
#   subclasses to handle the specific data 
#   needs of individuals versus companies.
# - **Requirements:**
#     - **Classes:** Client with attributes company_name, 
#       email, and contract_value.
#     - I**nheritance:** Create IndividualClient 
#       (adds phone) and CorporateClient 
#       (adds tax_id and representative_name)
#     - Logic: Implement a method get_tier() that 
#       returns **"VIP"** if contract_value > 10,000, 
#       otherwise **"Standard"**

import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

class Client():
    def __init__(self, company_name, email, contract_value):
        self.company_name = company_name
        self.email = email
        self.contract_value = contract_value
    
    def get_tier(self):
        # TODO
        if self.contract_value > 10000:
            return "VIP"
        else:
            return "Standard"
    
class IndividualClient(Client):
    def __init__(self, company_name, email, contract_value, phone):
        super().__init__(company_name, email, contract_value)
        self.phone = phone

class CorporateClient(Client):
    def __init__(self, company_name, email, contract_value, tax_id, representative_name):
        super().__init__(company_name, email, contract_value)
        self.tax_id = tax_id
        self.representative_name = representative_name
