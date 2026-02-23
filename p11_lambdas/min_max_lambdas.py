nombres = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# Encuentra la longitud mínima de un nombre en la lista nombres
print(min(len(nombre) for nombre in nombres))  # 3

# Encuentra el nombre más largo
print(max(nombres, key=lambda n: len(n)))  # Ollivander

canciones = [
    {"titulo": "feliz cumpleaños", "reproducciones": 1},
    {"titulo": "Sobrevivir", "reproducciones": 6},
    {"titulo": "YMCA", "reproducciones": 99},
    {"titulo": "Toxico", "reproducciones": 31}
]

# Encuentra la canción con el menor número de reproducciones
print(min(canciones, key=lambda c: c['reproducciones']))
# {"titulo": "feliz cumpleaños", "reproducciones": 1}

# Encuentra el título de la canción más reproducida
print(max(canciones, key=lambda c: c['reproducciones'])['titulo'])
# YMCA
