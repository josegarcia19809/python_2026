# 1️⃣ Revertir una lista
numeros = [1, 2, 3, 4, 5]

resultado = reversed(numeros)
print(list(resultado))

print("-" * 100)
# 🔹 2️⃣ Recorrer una lista al revés con un ciclo
colores = ["rojo", "azul", "verde"]

for color in reversed(colores):
    print(color)

print("-" * 100)

# 🔹 3️⃣ Revertir una tupla
numeros = (10, 20, 30, 40)
print(tuple(reversed(numeros)))

# 🔹 4️⃣ Revertir una cadena (string)
print("-" * 100)
texto = "python"
print("".join(reversed(texto)))

print("-" * 100)
# 🔹 5️⃣ Revertir un rango
for numero in reversed(range(1, 6)):
    print(numero)

print("-" * 100)
