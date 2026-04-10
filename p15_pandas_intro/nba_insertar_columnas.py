import pandas as pd

nba = pd.read_csv("data/nba.csv")

print(nba.head())

# Insertar una columna al final
nba["Deporte"] = "Basketball"
print(nba.head())

# Insertar columna en una determinada posición
nba.insert(loc=2, column="Año", value=2026)
print(nba.head())

# Insertar una columna después de aplicar una operación
nba["Salario duplicado"] = nba["Salario"] * 2
print(nba.head())

nba.insert(
    loc=5,
    column="Salario con Descuento",
    value=nba["Salario duplicado"] * 0.90
)
columnas = ["Nombre","Salario","Salario duplicado", "Salario con Descuento"]
print(nba[columnas])
print(nba.info())