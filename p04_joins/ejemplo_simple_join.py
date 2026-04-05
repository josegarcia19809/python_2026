import time
from threading import Thread


def hilo_hijo():
    print("Hilo hijo trabajando...")
    time.sleep(5)
    print("Hilo hijo terminado...")


def hilo_padre():
    hilo = Thread(target=hilo_hijo, args=())
    hilo.start()
    print("Hilo padre esperando...")
    hilo.join()
    print("Hilo padre desbloqueado...")


hilo_padre()