import pandas as pd

print("📂 Cargando el archivo cafeterias.csv...")
cafeterias = pd.read_csv("data/cafeterias.csv")

print("\n🔎 Primeras filas del dataset:")
print(cafeterias.head())
print()

print("☕ Ordenar las cafeterías primero por Ciudad y después por Cafeteria (orden ascendente por defecto)")
print(cafeterias.sort_values(["Ciudad", "Cafeteria"]))
print()

print("☕ Ordenar las cafeterías por Ciudad y Cafeteria usando el parámetro by")
print(cafeterias.sort_values(by=["Ciudad", "Cafeteria"]))
print()

print("⬆️ Ordenar por Ciudad y Cafeteria en orden ascendente")
print(cafeterias.sort_values(by=["Ciudad", "Cafeteria"], ascending=True))
print()

print("⬇️ Ordenar por Ciudad y Cafeteria en orden descendente")
print(cafeterias.sort_values(by=["Ciudad", "Cafeteria"], ascending=False))
print()

print("🔀 Ordenar por Ciudad (ascendente) y Cafeteria (descendente)")
print(cafeterias.sort_values(by=["Ciudad", "Cafeteria"], ascending=[True, False]))
print()

print("🏙️ Ordenar cafeterías por Ciudad y luego por Ingreso_Semanal")
print(cafeterias.sort_values(["Ciudad", "Ingreso_Semanal"]))
print()

print("⬆️ Ordenar por Ciudad e Ingreso_Semanal en orden ascendente")
print(cafeterias.sort_values(["Ciudad", "Ingreso_Semanal"], ascending=True))
print()

print("⬇️ Ordenar por Ciudad e Ingreso_Semanal en orden descendente")
print(cafeterias.sort_values(["Ciudad", "Ingreso_Semanal"], ascending=False))
print()

print("🔀 Ordenar por Ciudad (ascendente) e Ingreso_Semanal (descendente)")
print(cafeterias.sort_values(["Ciudad", "Ingreso_Semanal"], ascending=[True, False]))
print()

print("🔀 Ordenar por Ciudad (descendente) e Ingreso_Semanal (ascendente)")
print(cafeterias.sort_values(["Ciudad", "Ingreso_Semanal"], ascending=[False, True]))
print()

print("💾 Guardar el DataFrame ordenado por Ciudad (descendente) e Ingreso_Semanal (ascendente)")
cafeterias = cafeterias.sort_values(["Ciudad", "Ingreso_Semanal"], ascending=[False, True])

print("\n📊 DataFrame final ordenado:")
print(cafeterias)