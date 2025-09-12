import pandas as pd

file_path = "data/datos_prueba.xlsx"
df = pd.read_excel(file_path)

print(df.shape)
df.head()
