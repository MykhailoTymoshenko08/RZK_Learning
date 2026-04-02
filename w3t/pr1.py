# Уяви, що тобі прилетіли результати з твого CV-проекту (AI Terminal) 
# у форматі CSV, але тобі треба зберегти їх у базу PostgreSQL для веб-дашборду.

# Створи CSV файл (просто кодом):

# Python
# temp_df = pd.DataFrame({'event': ['check-in', 'check-out'], 'worker_id': [101, 102]})
# temp_df.to_csv('events.csv', index=False)

# Завдання: Прочитай цей events.csv, додай до нього нову колонку 
# status зі значенням "processed" і збережи результат у новий 
# файл processed_events.csv.


import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()



try:
    posgresql_engine = create_engine(os.getenv('DB_URL'))
    dataset = pd.read_csv("./events.csv", sep=',', header=0)
    dataset.to_sql('w3t_p', posgresql_engine, if_exists='replace')
except:
    pass

