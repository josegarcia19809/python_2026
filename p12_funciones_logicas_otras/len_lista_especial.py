class ListaEspecial:

    # Constructor de la clase
    def __init__(self, datos):
        # Guardamos los datos en un atributo privado
        self.__datos = datos

    # Este método especial se ejecuta cuando usamos len(objeto)
    def __len__(self):
        # Sin importar cuántos elementos tenga la lista,
        # siempre devolverá 50
        return 50


# Creamos dos objetos con listas diferentes
lista1 = ListaEspecial([1, 40, 30, 100, 30, 1, 2, 3, 4])
lista2 = ListaEspecial([1, 3, 4, 5])

# Aunque las listas tienen tamaños distintos,
# el método __len__ está programado para devolver siempre 50
print(len(lista1))  # 50
print(len(lista2))  # 50
