from threading import Thread, Lock
import time


def robot_rojo(candado1, candado2):
    while True:
        print("Rojo: Adquiriendo candado 1...")
        candado1.acquire()
        time.sleep(0.1)

        print("Rojo: Adquiriendo candado 2...")
        candado2.acquire()

        print("Rojo: Candados adquiridos...")

        candado1.release()
        candado2.release()

        print("Rojo: Candados liberados")
        time.sleep(0.5)


def robot_azul(candado1, candado2):
    while True:
        print("Azul: Adquiriendo candado 2...")
        candado2.acquire()
        time.sleep(0.1)

        print("Azul: Adquiriendo candado 1...")
        candado1.acquire()

        print("Azul: Candados adquiridos...")

        candado1.release()
        candado2.release()

        print("Azul: Candados liberados")
        time.sleep(0.5)


mutex1 = Lock()
mutex2 = Lock()

rojo = Thread(target=robot_rojo, args=(mutex1, mutex2))
azul = Thread(target=robot_azul, args=(mutex1, mutex2))

rojo.start()
azul.start()
