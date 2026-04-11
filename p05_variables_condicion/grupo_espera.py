from threading import Condition


class GrupoEspera:
    contador_espera = 0
    condicion = Condition()

    def agregar(self, cantidad):
        self.condicion.acquire()
        self.contador_espera += cantidad
        self.condicion.release()

    def terminado(self):
        self.condicion.acquire()
        if self.contador_espera > 0:
            self.contador_espera -= 1
        if self.contador_espera == 0:
            self.condicion.notify_all()
        self.condicion.release()

    def esperar(self):
        self.condicion.acquire()
        while self.contador_espera > 0:
            self.condicion.wait()
        self.condicion.release()
