# all_funcion_logica

# Ejemplo 1: Todos positivos
numeros = [4, 7, 2, 9]
todos_positivos = all(numero > 0 for numero in numeros)
print(todos_positivos)

# True
# ✔ Porque todos son mayores que 0.

# ✅ Ejemplo 2: Uno es negativo
numeros = [4, -7, 2, 9]
todos_positivos = all(numero > 0 for numero in numeros)
print(todos_positivos)

# False
# ✔ Porque hay un número negativo.

# ✅ Ejemplo 3: Lista vacía

valores = []
print(all(valores))
# True
# ⚠ Esto puede sorprender:
# all([]) devuelve True porque no existe ningún elemento falso.


# 🧠 Diferencia rápida
# Función	¿Cuándo devuelve True?
# any()	Si al menos uno es verdadero
# all()	Si todos son verdaderos