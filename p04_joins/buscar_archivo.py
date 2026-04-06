import os
import time
from os.path import isdir, join

coincidencias = []


def buscar_archivo(ruta_raiz, nombre_archivo):
    print(f"Buscando en: {ruta_raiz} 🔎")

    for archivo in os.listdir(ruta_raiz):
        ruta_completa = os.path.join(ruta_raiz, archivo)

        # Si encontramos el archivo
        if nombre_archivo in archivo:
            coincidencias.append(ruta_completa)  # Guardar resultado 📍

        # Si es carpeta, buscar dentro (recursividad)
        if os.path.isdir(ruta_completa):
            buscar_archivo(ruta_completa, nombre_archivo)


def main():
    inicio = time.time()  # ⏱️ Inicio del tiempo

    # buscar_archivo("C:/tools", "README.md")
    buscar_archivo("/Users/josegarcia/Documents/", "README.md")

    fin = time.time()  # ⏱️ Fin del tiempo

    for resultado in coincidencias:
        print("Coincidencia:", resultado)

    print(f"\nTiempo total de búsqueda: {fin - inicio:.4f} segundos ⏳")
    print(f"Coincidencias: {len(coincidencias)}")


main()