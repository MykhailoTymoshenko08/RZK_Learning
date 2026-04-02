# Уяви, що в твоєму dataset з AI Terminal є 1000 рядків.

# Завдання 3.1: Використай .iloc, щоб вивести рядки з 10-го по 
# 15-й (включно) та тільки перші дві колонки.

# Завдання 3.2: Використай фільтрацію, щоб знайти всі події, 
# де worker_id дорівнює 101.

# Завдання 3.3 (зірочка): Знайди всі записи, де worker_id більше 
# 100 АБО подія (event) — це check-out.

import pandas as pd

dataset = pd.read_csv("./datas.csv")
subset = dataset.iloc[10:15, 0:2]
filtered = dataset[dataset['worker_id'] == 101]
stared = dataset[(dataset['worker_id'] > 100) | (dataset['event'] == 'check-out')]