from multiprocessing import Process, Queue
import multiprocessing
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
        time.sleep(1)


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    cola = Queue(maxsize=10)

    proceso1 = Process(
        target=consumidor,
        args=(cola,)
    )

    proceso2 = Process(
        target=productor,
        args=(cola,)
    )

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()
