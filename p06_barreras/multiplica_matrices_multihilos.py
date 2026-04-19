import time
from random import Random

from threading import Barrier, Thread

tamano_matriz = 200
matriz_a = [[0] * tamano_matriz for a in range(tamano_matriz)]
matriz_b = [[0] * tamano_matriz for b in range(tamano_matriz)]
resultado = [[0] * tamano_matriz for r in range(tamano_matriz)]
aleatorio = Random()
inicio_trabajo = Barrier(tamano_matriz + 1)
fin_trabajo = Barrier(tamano_matriz + 1)


def generar_matriz_aleatoria(matriz):
    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            matriz[fila][columna] = aleatorio.randint(-5, 5)


def calcular_fila(fila):
    while True:
        inicio_trabajo.wait()
        for columna in range(tamano_matriz):
            for i in range(tamano_matriz):
                resultado[fila][columna] += matriz_a[fila][i] * matriz_b[i][columna]
        fin_trabajo.wait()


for fila in range(tamano_matriz):
    Thread(target=calcular_fila, args=([fila])).start()

inicio = time.time()
for t in range(10):
    generar_matriz_aleatoria(matriz_a)
    generar_matriz_aleatoria(matriz_b)
    resultado = [[0] * tamano_matriz for r in range(tamano_matriz)]
    inicio_trabajo.wait()
    fin_trabajo.wait()

fin = time.time()
print("Terminado, tiempo transcurrido", fin - inicio)
