import pandas as pd

basket = pd.read_csv("data/estadisticas_equipo_basket.csv")

print(basket.head())

# Insertar una columna al final
basket["Deporte"] = "Basketball"
print(basket.head())

# Insertar columna en una posición específica
basket.insert(loc=2, column="Temporada", value=2026)
print(basket.head())

# Crear una columna con una operación
# Convierte las columnas a numéricas antes de hacer la operación.
basket["Canastas anotadas"] = pd.to_numeric(basket["Canastas anotadas"], errors="coerce")
basket["Asistencias"] = pd.to_numeric(basket["Asistencias"], errors="coerce")
basket["Rebotes"] = pd.to_numeric(basket["Rebotes"], errors="coerce")

basket["Total acciones"] = (
    basket["Canastas anotadas"] +
    basket["Asistencias"] +
    basket["Rebotes"]
)

print(basket.head())

# Insertar una columna calculada
basket.insert(
    loc=5,
    column="Impacto del jugador",
    value=basket["Total acciones"] * 0.90
)

# Mostrar algunas columnas
columnas = [
    "Jugador",
    "Canastas anotadas",
    "Total acciones",
    "Impacto del jugador"
]

print(basket[columnas])

# Información del DataFrame
print(basket.info())
