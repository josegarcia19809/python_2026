import time
from random import Random

tamano_matriz = 200

matriz_a = [[0] * tamano_matriz for a in range(tamano_matriz)]
matriz_b = [[0] * tamano_matriz for b in range(tamano_matriz)]
resultado = [[0] * tamano_matriz for r in range(tamano_matriz)]
aleatorio = Random()


def generar_matriz_aleatoria(matriz):
    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            matriz[fila][columna] = aleatorio.randint(-5, 5)


inicio = time.time()
for t in range(10):
    generar_matriz_aleatoria(matriz_a)
    generar_matriz_aleatoria(matriz_b)
    resultado = [[0] * tamano_matriz for r in range(tamano_matriz)]
    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            for i in range(tamano_matriz):
                resultado[fila][columna] += matriz_a[fila][i] * matriz_b[i][columna]

#   for fila in range(tamano_matriz):
#       print(matriz_a[fila], matriz_b[fila], resultado[fila])
#       print()
fin = time.time()
print("Terminado, tiempo transcurrido", fin - inicio)
