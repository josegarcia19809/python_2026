import pandas as pd

nba = pd.read_csv("data/nba.csv")

print(nba.head())

# Ver cuántas veces aparece cada equipo
print(nba["Equipo"].value_counts())

# Ver el porcentaje en la que aparece cada equipo
print(nba["Equipo"].value_counts(normalize=True) * 100)
