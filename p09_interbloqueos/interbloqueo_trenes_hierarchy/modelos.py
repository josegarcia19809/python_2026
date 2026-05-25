class Tren:
    def __init__(self, identificador, longitud_tren, frente):
        self.identificador = identificador
        self.longitud_tren = longitud_tren
        self.frente = frente


class Interseccion:
    def __init__(self, identificador, mutex, bloqueado_por):
        self.identificador = identificador
        self.mutex = mutex
        self.bloqueado_por = bloqueado_por


class Cruce:
    def __init__(self, posicion, interseccion):
        self.posicion = posicion
        self.interseccion = interseccion