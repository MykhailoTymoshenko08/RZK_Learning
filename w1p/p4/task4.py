# - Currency converter with data caching
# - **Essence:** Working with APIs and processing complex structures.
# - **TT:** The program connects to an API (for example, NBU or PrivatBank), 
# loads currency rates. If the internet disappears, it should take data 
# from a local file (cache) that was saved last time.


import json
import requests

FILENAME = "data.json"
URL = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"


try:
    response = requests.get(URL)
    data = response.json()
    print("\tCurrency Base Cureency\t | Buy / Sale")
    print("\t---------------------------------------------")
    for cur in data:
        print(f"\t{cur["ccy"]}\t {cur["base_ccy"]}\t\t | {cur["buy"]}/{cur["sale"]}")

    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)
except:
    print("No internet connection, loading cache...")
    try:
        with open(FILENAME, "r") as f:
            dataset = json.load(f)
        print("\tCurrency Base Cureency\t | Buy / Sale")
        print("\t---------------------------------------------")
        for cur in dataset:
            print(f"\t{cur["ccy"]}\t {cur["base_ccy"]}\t\t | {cur["buy"]}/{cur["sale"]}")
    except:
        print("No cache available")

