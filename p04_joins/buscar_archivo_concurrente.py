import os
import time
from os.path import isdir, join
from threading import Lock, Thread

mutex = Lock()
coincidencias = []


def buscar_archivo(ruta_raiz, nombre_archivo):
    print("Buscando en:", ruta_raiz)
    hilos_hijos = []

    for archivo in os.listdir(ruta_raiz):
        ruta_completa = join(ruta_raiz, archivo)

        if nombre_archivo in archivo:
            mutex.acquire()
            coincidencias.append(ruta_completa)
            mutex.release()

        if isdir(ruta_completa):
            hilo = Thread(target=buscar_archivo, args=([ruta_completa, nombre_archivo]))
            hilo.start()
            hilos_hijos.append(hilo)

    for hilo in hilos_hijos:
        hilo.join()


def main():
    inicio = time.time()  # ⏱️ inicio

    hilo_principal = Thread(
        target=buscar_archivo,
        # args=("c:/tools", "README.md")
        args=(["/Users/josegarcia/Documents/", "README.md"])
    )
    hilo_principal.start()
    hilo_principal.join()

    fin = time.time()  # ⏱️ fin

    for resultado in coincidencias:
        print("Coincidencia:", resultado)

    print(f"\nTiempo total de búsqueda: {fin - inicio:.4f} segundos ⏳")
    print(f"Coincidencias: {len(coincidencias)}")


main()
