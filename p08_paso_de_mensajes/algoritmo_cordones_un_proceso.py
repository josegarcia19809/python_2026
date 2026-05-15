import re
import time

# (45,11),(41,15),(36,20)

REGEX_PUNTOS = r"\((\d*),(\d*)\)"


def encontrar_area(cadena_puntos):
    puntos = []
    area = 0.0

    for xy in re.finditer(REGEX_PUNTOS, cadena_puntos):
        puntos.append((int(xy.group(1)), int(xy.group(2))))

    for i in range(len(puntos)):
        a, b = puntos[i], puntos[(i + 1) % len(puntos)]
        area += a[0] * b[1] - a[1] * b[0]

    area = abs(area) / 2.0

    # print(area)


archivo = open("poligonos.txt", "r")

lineas = archivo.read().splitlines()

inicio = time.time()

for linea in lineas:
    encontrar_area(linea)

fin = time.time()

print("Tiempo transcurrido:", fin - inicio)
