numeros = [0, 0, 3, 0]
resultado = any(numeros)
print(resultado)
# True
# ✔ Porque existe un valor distinto de 0 (el 3).
# (En Python, 0 es False y cualquier número distinto de 0 es True).

print("-" * 100)

datos = []
print(any(datos))

# False
# ✔ Porque no hay ningún elemento verdadero.

print("-" * 100)

numeros = [5, 8, -2, 10]
hay_negativo = any(numero < 0 for numero in numeros)
print(hay_negativo)
# True
# ✔ Porque existe al menos un número negativo.

print("-" * 100)
