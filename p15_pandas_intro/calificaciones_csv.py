# calificaciones_csv
import pandas as pd


def imprimir_linea():
    print("-" * 60)


calificaciones_df = pd.read_csv("data/calificaciones.csv")
print(calificaciones_df.head())
imprimir_linea()
