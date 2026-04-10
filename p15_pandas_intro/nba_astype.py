# ## El método astype I
# - El método `astype` convierte los valores de una **Series** a un tipo de dato específico.
# - Puedes pasar el tipo de dato como una cadena de texto (string) o como el tipo de dato nativo de Python.
# - Pandas no puede convertir valores `NaN` a tipos numéricos, por lo que primero debemos eliminarlos o reemplazarlos antes de realizar la conversión.
# - El atributo `dtypes` devuelve una **Series** con las columnas del **DataFrame** y sus respectivos tipos de datos.

# Leemos el archivo nba.csv
# dropna(how="all") elimina las filas que estén completamente vacías (todas sus columnas en NaN)

import pandas as pd
nba = pd.read_csv("data/nba.csv").dropna(how="all")

print("DataFrame después de eliminar filas completamente vacías:")
print(nba)

# Reemplazamos los valores NaN en la columna "Salario" por 0
# Esto es importante porque los valores numéricos no pueden convertirse si contienen NaN
nba["Salario"] = nba["Salario"].fillna(0)

# Reemplazamos los valores NaN en la columna "Peso" por 0
nba["Peso"] = nba["Peso"].fillna(0)

print("\nDataFrame después de rellenar Salario y Peso con 0:")
print(nba)

# El atributo dtypes muestra el tipo de dato de cada columna del DataFrame
print("Tipos de datos de cada columna:")
print(nba.dtypes)

# Convierte la columna "Salario" a tipo entero usando string
# IMPORTANTE: Esto NO modifica el DataFrame original
nba["Salario"].astype("int")

# Convierte la columna "Salario" a tipo entero usando el tipo nativo de Python
# Tampoco modifica el DataFrame porque no se está reasignando
nba["Salario"].astype(int)

print()
print("Tipo de dato antes de reasignar:")
print(nba["Salario"].dtype)


# Aquí sí estamos guardando el resultado
# Ahora la columna "Salario" cambia permanentemente a tipo entero
nba["Salario"] = nba["Salario"].astype(int)


print("\nTipo de dato después de reasignar:")
print(nba["Salario"].dtype)

# Convertimos la columna "Peso" a tipo entero (int)
# IMPORTANTE: Solo funcionará si ya no existen valores NaN en la columna
nba["Peso"] = nba["Peso"].astype(int)

print()
# Verificamos el nuevo tipo de dato
print("Tipo de dato de la columna Peso después de la conversión:")
print(nba["Peso"].dtype)