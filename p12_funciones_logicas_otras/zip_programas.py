print("EJEMPLO 1: Unir nombres con edades")

# Lista de nombres (cadenas)
nombres = ["Ana", "Luis", "Carlos"]

# Lista de edades (números)
edades = [20, 22, 19]

# zip une elemento por elemento
resultado = zip(nombres, edades)

# Convertimos a lista para visualizar
print(list(resultado))

print("-" * 100)

print("EJEMPLO 2: Recorrer con for")

materias = ["Matemáticas", "Historia", "Química"]
calificaciones = [9, 8, 10]

# Se recorren ambas listas al mismo tiempo
for materia, calificacion in zip(materias, calificaciones):
    print(materia, "->", calificacion)

print("-" * 100)
print("EJEMPLO 3: Crear un diccionario")

productos = ["Laptop", "Mouse", "Teclado"]
precios = [15000, 300, 800]

# zip permite crear un diccionario fácilmente
diccionario_productos = dict(zip(productos, precios))

print(diccionario_productos)

print("-" * 100)
print("EJEMPLO 4: Listas de diferente tamaño")

letras = ["A", "B", "C", "D"]
numeros = [1, 2]

# zip se detiene cuando la lista más corta termina
print(list(zip(letras, numeros)))

print("-" * 100)
print("EJEMPLO 5: Operaciones con zip")

numeros1 = [10, 20, 30]
numeros2 = [1, 2, 3]

# Sumar elementos correspondientes
suma = [a + b for a, b in zip(numeros1, numeros2)]

print(suma)

print("-" * 100)
