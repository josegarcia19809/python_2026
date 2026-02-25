print("EJEMPLO 1: Desempaquetar listas con zip(*)")

pares = [("Ana", 20), ("Luis", 22), ("Carlos", 19)]

# El operador * desempaqueta la lista
nombres, edades = zip(*pares)

print("Nombres:", nombres)
print("Edades:", edades)

print("-" * 100)

# 📌 Aquí zip(*pares) separa las tuplas en dos grupos:

# Todos los nombres
#
# Todas las edades

print("EJEMPLO 2: Separar números y letras")

datos = [(1, "A"), (2, "B"), (3, "C")]

numeros, letras = zip(*datos)

print("Números:", numeros)
print("Letras:", letras)

print("-" * 100)
print("EJEMPLO 3: Transponer una matriz")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transposición usando zip y *
transpuesta = list(zip(*matriz))

print("Matriz original:", matriz)
print("Matriz transpuesta:", transpuesta)

print("-" * 100)

# 📌 Aquí el * desempaqueta cada fila como argumento separado para zip().

print("EJEMPLO 4: Volver a unir datos")

nombres = ("Ana", "Luis", "Carlos")
edades = (20, 22, 19)

# Volvemos a unirlos
datos_unidos = list(zip(nombres, edades))

print("Datos unidos:", datos_unidos)

print("-" * 100)
