from datetime import datetime
def filter_cust(dataset, **kwargs):
    min_amount = kwargs.get("min_amount")
    max_date = kwargs.get("max_date")

    #filtered = filter_cust(dataset, min_amount = x, max_date = "2026-02-16")
    filtered = []
    for i in range(len(dataset)):
        if dataset[i]["amount_spent"] > min_amount and dataset[i]["last_order_date"] < max_date:
            filtered.append(dataset[i])

    return filtered