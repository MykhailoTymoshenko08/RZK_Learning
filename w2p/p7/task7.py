# - **Essence:** Building a scalable structure to manage the diverse client base of RZK Soft
# - **TT:** Create a base class Client and specialized subclasses to handle the specific data 
#   needs of individuals versus companies.
# - **Requirements:**
#     - **Classes:** Client with attributes company_name, email, and contract_value.
#     - I**nheritance:** Create IndividualClient (adds phone) and CorporateClient 
#       (adds tax_id and representative_name)
#     - Logic: Implement a method get_tier() that returns **"VIP"** 
#       if contract_value > 10,000, otherwise **"Standard"**