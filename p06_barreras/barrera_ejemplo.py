import time
from threading import Barrier, Thread

barrera = Barrier(2)


def esperar_en_barrera(nombre, tiempo_de_espera):
    for i in range(10):
        print(nombre, "en ejecución")
        time.sleep(tiempo_de_espera)
        print(nombre, "está esperando en la barrera")
        barrera.wait()
    print(nombre, "ha terminado")


rojo = Thread(target=esperar_en_barrera, args=["rojo", 4])
azul = Thread(target=esperar_en_barrera, args=["azul", 10])
rojo.start()
azul.start()
# time.sleep(8)
# print("Abortando barrera")
# barrera.abort()
# barrera.reset()