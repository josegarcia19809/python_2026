import pandas as pd
import numpy as np

# Crear un diccionario con datos
datos = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [20, 22, 21],
    "Promedio": [8.5, 9.2, 8.8]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar información
print("DataFrame completo:")
print(df)
print("-" * 100)

print("\nPromedio general:")
print(np.mean(df["Promedio"]))
print("-" * 100)

print("\nInformación del DataFrame:")
print(df.info())
