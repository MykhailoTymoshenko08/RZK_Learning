# Уяви, що в твоєму dataset з AI Terminal:

# У колонці worker_id є пропуски. Завдання: Заповни їх числом 0.

# У колонці accuracy є пропуски. Завдання: Видали всі рядки, де accuracy порожня.

# Завдання: Видали дублікати, але тільки ті, де збігаються і worker_id, 
# і event одночасно. (Підказка: використовуй параметр subset=['col1', 'col2'] 
# у методі drop_duplicates).

import pandas as pd

dataset = pd.read_csv("dataset_file1.csv")

dataset['worker_id'] = dataset['worker_id'].fillna(0)
dataset = dataset.dropna(subset=['accuracy'], axis=0)
dataset.drop_duplicates(subset=['worker_id','event'], keep='first', inplace=True)