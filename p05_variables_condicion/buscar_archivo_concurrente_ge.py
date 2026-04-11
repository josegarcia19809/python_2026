import os
import time
from os.path import isdir, join
from threading import Lock, Thread

from grupo_espera import GrupoEspera

mutex = Lock()
coincidencias = []


def buscar_archivo(raiz, nombre_archivo, grupo_espera):
    print("Buscando en:", raiz)
    for archivo in os.listdir(raiz):
        ruta_completa = join(raiz, archivo)
        if nombre_archivo in archivo:
            mutex.acquire()
            coincidencias.append(ruta_completa)
            mutex.release()
        if isdir(ruta_completa):
            grupo_espera.agregar(1)
            t = Thread(target=buscar_archivo,
                       args=([ruta_completa, nombre_archivo, grupo_espera]))
            t.start()
    grupo_espera.terminado()


def main():
    inicio = time.time()  # ⏱️ inicio
    grupo_espera = GrupoEspera()
    grupo_espera.agregar(1)
    t = Thread(target=buscar_archivo,
               args=(["/Users/josegarcia/Documents/",
                      "README.md", grupo_espera])
               )
    t.start()
    grupo_espera.esperar()

    fin = time.time()  # ⏱️ fin

    for m in coincidencias:
        print("Coincidencia:", m)

    print(f"\nTiempo total de búsqueda: {fin - inicio:.4f} segundos ⏳")
    print(f"Coincidencias: {len(coincidencias)}")


main()
