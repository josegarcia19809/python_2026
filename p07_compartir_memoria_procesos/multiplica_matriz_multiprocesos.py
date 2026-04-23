import multiprocessing
import time
from random import Random

from multiprocessing import Barrier
from multiprocessing.context import Process

# ⚙️ Número de procesos (núcleos)
numero_procesos = 8

# 📏 Tamaño de la matriz (200x200)
tamano_matriz = 200

# 🎲 Generador de números aleatorios
aleatorio = Random()


# 🎲 Función para llenar una matriz con valores aleatorios
def generar_matriz_aleatoria(matriz):
    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            matriz[fila * tamano_matriz + columna] = aleatorio.randint(-5, 5)


# ⚙️ Función que ejecuta cada proceso
def calcular_filas(id_proceso, matriz_a, matriz_b, resultado, inicio_trabajo,
                   fin_trabajo):
    while True:
        # 🚧 Espera a que el proceso principal dé la señal de inicio
        inicio_trabajo.wait()

        # 🔁 Cada proceso trabaja en varias filas (saltando según su ID)
        for fila in range(id_proceso, tamano_matriz, numero_procesos):
            for columna in range(tamano_matriz):
                for i in range(tamano_matriz):
                    resultado[fila * tamano_matriz + columna] += (
                            matriz_a[fila * tamano_matriz + i] *
                            matriz_b[i * tamano_matriz + columna]
                    )

        # 🚧 Señal de que terminó su trabajo
        fin_trabajo.wait()


if __name__ == '__main__':
    # ⚙️ Método de inicio de procesos
    multiprocessing.set_start_method('spawn')

    # 🚧 Barreras para sincronizar procesos
    inicio_trabajo = Barrier(numero_procesos + 1)
    fin_trabajo = Barrier(numero_procesos + 1)

    # 🧠 Memoria compartida para matrices (1D)
    matriz_a = multiprocessing.Array('i', [0] * (tamano_matriz * tamano_matriz),
                                     lock=False)
    matriz_b = multiprocessing.Array('i', [0] * (tamano_matriz * tamano_matriz),
                                     lock=False)
    resultado = multiprocessing.Array('i', [0] * (tamano_matriz * tamano_matriz),
                                      lock=False)

    # 🚀 Crear procesos
    for p in range(numero_procesos):
        Process(
            target=calcular_filas,
            args=(p, matriz_a, matriz_b, resultado, inicio_trabajo, fin_trabajo)
        ).start()

    # ⏱️ Medir tiempo de ejecución
    inicio = time.time()

    for t in range(10):
        # 🎲 Generar matrices aleatorias
        generar_matriz_aleatoria(matriz_a)
        generar_matriz_aleatoria(matriz_b)

        # 🧼 Limpiar matriz resultado
        for i in range(tamano_matriz * tamano_matriz):
            resultado[i] = 0

        # 🚀 Iniciar cálculo
        inicio_trabajo.wait()

        # ⏳ Esperar a que todos terminen
        fin_trabajo.wait()

    fin = time.time()

    print("✅ Listo, tiempo total:", fin - inicio)
