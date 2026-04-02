import pandas as pd

# Буде 3 колонки: model_name (рядок), accuracy (float), detected_objects (int).
# Спеціально вкажи тип dtype для accuracy як float32 (це економить пам'ять на MacBook, 
# що важливо для великих моделей).
# Виведи df.info() та подивись, скільки пам'яті він займає.

df = pd.DataFrame({
    'model_name': ['YOLOv8', 'Faster R-CNN', 'SSD'],
    'accuracy': [0.94, 0.88, 0.75],
    'detected_objects': [15, 12, 10]
})
df['accuracy'] = df['accuracy'].astype('float32')
df['model_name'] = df['model_name'].astype('object')
df['detected_objects'] = df['detected_objects'].astype('int16')

df.info()

model_name = pd.Series(['YOLOv8', 'SSD'], dtype='object')
accuracy = pd.Series([0.94, 0.75], dtype='float32')

df = pd.DataFrame({
    'model_name': model_name,
    'accuracy': accuracy
})