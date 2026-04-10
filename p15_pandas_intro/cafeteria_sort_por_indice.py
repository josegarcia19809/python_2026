import pandas as pd

print("📂 Cargando el archivo cafeterias.csv...")
cafeterias = pd.read_csv("data/cafeterias.csv")

print("\n🔎 Primeras filas del DataFrame:")
print(cafeterias.head())
print()

print("🏙️ Ordenar el DataFrame primero por Ciudad y después por Cafeteria")
cafeterias = cafeterias.sort_values(["Ciudad", "Cafeteria"])

print("📊 DataFrame ordenado por columnas:")
print(cafeterias)
print()

print("🔢 Ordenar el DataFrame usando su índice (orden ascendente por defecto)")
print(cafeterias.sort_index())
print()

print("⬆️ Ordenar el índice de forma ascendente")
print(cafeterias.sort_index(ascending=True))
print()

print("⬇️ Ordenar el índice de forma descendente")
print(cafeterias.sort_index(ascending=False))
print()

print("💾 Guardar el DataFrame ordenado por índice en orden descendente")
cafeterias = cafeterias.sort_index(ascending=False)

print("\n📊 DataFrame final ordenado:")
print(cafeterias)
