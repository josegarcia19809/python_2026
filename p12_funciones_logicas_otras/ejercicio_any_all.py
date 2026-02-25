# 🎯 Ejercicio: Any / All
#
# Vamos a crear una función llamada is_all_strings 🧩
#
# Esta función debe:
#
# 👉 Recibir un iterable (lista, tupla, etc.)
# 👉 Revisar si todos sus elementos son cadenas de texto (str)
# 👉 Devolver True ✅ si solo contiene strings
# 👉 Devolver False ❌ si encuentra algo que no sea string
#
# 🧪 Ejemplos de uso
# is_all_strings(['a', 'b', 'c'])
# # True ✅
#
# is_all_strings([2, 'a', 'b', 'c'])
# # False ❌
#
# is_all_strings(('hello', 'goodbye'))
# # True ✅
#
#
# 💡 Pista: Puedes usar all() junto con type() o isinstance() para resolverlo de manera
# elegante.

def is_all_strings(valores):
    return all(type(valor) == str for valor in valores)


print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2, 'a', 'b', 'c']))
print(is_all_strings(('hello', 'goodbye')))

# ✅ Solución: is_all_strings
#
# Vamos a resolver el ejercicio paso a paso 🚀
#
# La idea es usar la función built-in all() para verificar que cada elemento sea un str.
#
# 🔹 Opción 1: Usando una Generator Expression ⚡ (Recomendada)
#
# Primero definimos la función is_all_strings, que recibe un parámetro llamado lst.
#
# Luego usamos all() y le pasamos una generator expression que revisa si cada elemento es de tipo str.
#
# def is_all_strings(lst):
#     return all(type(l) == str for l in lst)
#
#
# 🧠 ¿Qué está pasando aquí?
#
# for l in lst → Recorremos cada elemento
#
# type(l) == str → Verificamos si es string
#
# all(...) → Devuelve True solo si todos cumplen la condición
#
# ✨ Es una forma más eficiente y elegante.
#
# 🔹 Opción 2: Usando List Comprehension 📋
#
# También puedes hacerlo creando primero una lista de valores True o False y luego evaluarla con all().
#
# def is_all_strings(lst):
#     return all([type(l) == str for l in lst])
#
#
# La única diferencia es que aquí usamos corchetes [] para crear una lista completa antes de evaluarla.
#
# 🎯 Nota importante
#
# ⚠ No te preocupes si las generator expressions aún no son totalmente claras.
#
# 👉 Más adelante en el curso hablaremos mucho más sobre generadores y verás por qué son tan útiles 😎
