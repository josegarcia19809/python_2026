import re
import time
from multiprocessing import Process, Queue

# (45,11),(41,15),(36,20)

REGEX_PUNTOS = r"\((\d*),(\d*)\)"

TOTAL_PROCESOS = 8


def encontrar_area(cola_puntos):
    cadena_puntos = cola_puntos.get()

    while cadena_puntos is not None:

        puntos = []
        area = 0.0

        for xy in re.finditer(REGEX_PUNTOS, cadena_puntos):
            puntos.append(
                (
                    int(xy.group(1)),
                    int(xy.group(2))
                )
            )

        for i in range(len(puntos)):
            a, b = puntos[i], puntos[(i + 1) % len(puntos)]

            area += a[0] * b[1] - a[1] * b[0]

        area = abs(area) / 2.0

        # print(area)

        cadena_puntos = cola_puntos.get()


if __name__ == '__main__':

    cola = Queue(maxsize=1000)

    procesos = []

    for i in range(TOTAL_PROCESOS):
        proceso = Process(
            target=encontrar_area,
            args=(cola,)
        )

        procesos.append(proceso)

        proceso.start()

    archivo = open("poligonos.txt", "r")

    lineas = archivo.read().splitlines()

    inicio = time.time()

    for linea in lineas:
        cola.put(linea)

    for _ in range(TOTAL_PROCESOS):
        cola.put(None)

    for proceso in procesos:
        proceso.join()

    fin = time.time()

    print("Tiempo transcurrido:", fin - inicio)
