# Уяви, що ми аналізуємо результати твого хакатону для RZK Soft. 
# У тебе є DataFrame з колонками team_name, score (0-100) та is_finished (True/False).

# Завдання 5.1: Використай .map(), щоб замінити True на 'Готово', а False на 'В процесі'.

# Завдання 5.2: Використай .apply() з lambda, щоб створити колонку bonus_score, 
# яка додає 10% до score (тобто score * 1.1).

# Завдання 5.3 (Бонус): Напиши функцію та використай .apply(..., axis=1), 
# щоб створити колонку final_status. Логіка: якщо score > 90 і проект 'Готово', 
# то статус — 'Winner', інакше — 'Participant'.

import pandas as pd
dataset = pd.read_csv("dataset_file1.csv")

status_map = {
    True: 'Ready',
    False: 'In process'
}
dataset['is_finished'] = dataset['is_finished'].map(status_map)

add_func = lambda score: score*1.1 
dataset['bonus_score'] = dataset['score'].apply(add_func)

def some_func(row):
    if row['score'] > 90 and row['is_finished'] == 'Ready':
        return "Winner"
    else:
        return "Participant"

dataset['final_status'] = dataset.apply(some_func, axis = 1)