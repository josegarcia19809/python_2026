# El método astype
# Convierte columnas a un tipo de dato específico

import pandas as pd

basket = pd.read_csv("data/estadisticas_equipo_basket.csv").dropna(how="all")

print("DataFrame después de eliminar filas completamente vacías:")
print(basket)

# Rellenamos valores faltantes
basket["Canastas anotadas"] = basket["Canastas anotadas"].fillna(0)
basket["Asistencias"] = basket["Asistencias"].fillna(0)
basket["Rebotes"] = basket["Rebotes"].fillna(0)

print("\nDataFrame después de rellenar valores faltantes:")
print(basket)

# Mostrar tipos de datos
print("Tipos de datos de cada columna:")
print(basket.dtypes)

# Convertir columna a entero (sin reasignar)
basket["Canastas anotadas"].astype("int")
basket["Canastas anotadas"].astype(int)

print()
print("Tipo de dato antes de reasignar:")
print(basket["Canastas anotadas"].dtype)

# Guardar la conversión
basket["Canastas anotadas"] = basket["Canastas anotadas"].astype(int)

print("\nTipo de dato después de reasignar:")
print(basket["Canastas anotadas"].dtype)

# Convertir otras columnas
basket["Asistencias"] = basket["Asistencias"].astype(int)
basket["Rebotes"] = basket["Rebotes"].astype(int)

print()
print("Tipos de datos después de la conversión:")
print(basket.dtypes)
