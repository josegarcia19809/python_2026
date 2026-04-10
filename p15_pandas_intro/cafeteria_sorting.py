import pandas as pd

cafeterias = pd.read_csv("data/cafeterias.csv")

print(cafeterias.head())

print("Ordenar las cafeterías por nombre (orden ascendente por defecto)")
print(cafeterias.sort_values("Cafeteria"))
print()

print("Ordenar las cafeterías por nombre usando el parámetro by")
print(cafeterias.sort_values(by="Cafeteria"))
print()

print("Ordenar las cafeterías por nombre en orden ascendente")
print(cafeterias.sort_values(by="Cafeteria", ascending=True))
print()

print("Ordenar las cafeterías por nombre en orden descendente")
print(cafeterias.sort_values(by="Cafeteria", ascending=False))
print()

print("Ordenar las cafeterías por ingreso semanal (de menor a mayor)")
print(cafeterias.sort_values("Ingreso_Semanal"))
print()

print("Ordenar las cafeterías por ingreso semanal (de mayor a menor)")
print(cafeterias.sort_values("Ingreso_Semanal", ascending=False))
print()

print("Ordenar por ingreso semanal colocando los valores faltantes (NaN) al final")
print(cafeterias.sort_values("Ingreso_Semanal", na_position="last"))
print()

print("Ordenar por ingreso semanal colocando los valores faltantes (NaN) al inicio")
print(cafeterias.sort_values("Ingreso_Semanal", na_position="first"))
print()

print("Ordenar por ingreso semanal de mayor a menor y colocando los NaN al inicio")
print(cafeterias.sort_values("Ingreso_Semanal", na_position="first", ascending=False))
