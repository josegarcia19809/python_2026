# ===================== FUNCIÓN abs() =====================

# abs() devuelve el valor absoluto de un número
# (es decir, lo convierte en positivo si es negativo)

numero1 = -25
numero2 = 10

print("Valor absoluto de -25:", abs(numero1))  # 25
print("Valor absoluto de 10:", abs(numero2))  # 10

print("-" * 100)

# ===================== FUNCIÓN sum() =====================

# sum() suma todos los elementos de un iterable (lista, tupla, etc.)

numeros = [5, 10, 15, 20]

resultado = sum(numeros)  # Suma todos los elementos de la lista

print("La suma de la lista es:", resultado)  # 50

# También podemos agregar un valor inicial
resultado_con_inicio = sum(numeros, 100)

print("La suma con valor inicial 100 es:", resultado_con_inicio)  # 150

print("-" * 100)

# ===================== FUNCIÓN round() =====================

# round() redondea un número decimal

numero_decimal = 8.56789

# Redondea al entero más cercano
print("Redondeado sin decimales:", round(numero_decimal))  # 9

# Redondea a 2 decimales
print("Redondeado a 2 decimales:", round(numero_decimal, 2))  # 8.57

# Ejemplo donde el redondeo baja
print("Redondear 8.3:", round(8.3))  # 8

print("-" * 100)
