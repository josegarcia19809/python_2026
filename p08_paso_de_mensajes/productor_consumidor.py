from queue import Queue
from threading import Thread

import time


def consumidor(cola):
    while True:
        texto = cola.get()
        print(texto)
        time.sleep(1)


def productor(cola):
    while True:
        cola.put("Hola")
        print("Mensaje enviado")


cola = Queue(maxsize=10)

hilo1 = Thread(target=consumidor, args=(cola,))
hilo2 = Thread(target=productor, args=(cola,))

hilo1.start()
hilo2.start()