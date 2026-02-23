usuarios = [
    {"nombre_usuario": "samuel",
     "publicaciones": ["Me encanta el pastel", "Me encanta el pay", "¡hola mundo!"]},
    {"nombre_usuario": "katie", "publicaciones": ["Amo a mi gato"]},
    {"nombre_usuario": "jeff", "publicaciones": [], "color": "morado"},
    {"nombre_usuario": "bob123", "publicaciones": [], "numero": 10,
     "color": "verde_azulado"},
    {"nombre_usuario": "amante_perros",
     "publicaciones": ["los perros son los mejores", "Tengo hambre"]},
    {"nombre_usuario": "chica_guitarra", "publicaciones": []}
]

# Ordenar usuarios por su nombre de usuario
usuarios_ordenados_nombre = sorted(usuarios,
                                   key=lambda usuario: usuario['nombre_usuario'])
print(usuarios_ordenados_nombre)

# Encontrar a nuestros usuarios más activos...
# Ordenar usuarios por número de publicaciones, de forma descendente
usuarios_mas_activos = sorted(usuarios, key=lambda usuario: len(usuario["publicaciones"]),
                              reverse=True)
print(usuarios_mas_activos)

# OTRO CONJUNTO DE DATOS DE EJEMPLO==================================
canciones = [
    {"titulo": "feliz cumpleaños", "reproducciones": 1},
    {"titulo": "Sobreviviré", "reproducciones": 6},
    {"titulo": "YMCA", "reproducciones": 99},
    {"titulo": "Tóxico", "reproducciones": 31}
]

# Ordenar canciones por número de reproducciones
canciones_por_reproducciones = sorted(canciones, key=lambda c: c['reproducciones'])
print(canciones_por_reproducciones)
