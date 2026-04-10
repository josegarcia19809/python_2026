import pandas as pd

basket = pd.read_csv("data/estadisticas_equipo_basket.csv")

print(basket.head())

# Ver cuántas veces aparece cada posición
print(basket["Posición"].value_counts())

# Ver el porcentaje en la que aparece cada posición
print(basket["Posición"].value_counts(normalize=True) * 100)
