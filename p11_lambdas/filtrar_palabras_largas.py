palabras = ["sol", "computadora", "mesa", "programacion"]

largas = list(filter(lambda palabra: len(palabra) > 5, palabras))

print(largas)
