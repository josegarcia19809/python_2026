import multiprocessing
from multiprocessing.context import Process
import time


def imprimir_contenido_arreglo(arreglo):
    # 🔁 Bucle infinito para mostrar el arreglo cada segundo
    while True:
        print(*arreglo, sep=", ")
        time.sleep(1)


if __name__ == '__main__':
    # ⚙️ Método de inicio para crear procesos (recomendado en algunos sistemas)
    multiprocessing.set_start_method('spawn')

    # 📦 Creamos un arreglo en memoria compartida (inicializado con -1)
    arreglo = multiprocessing.Array('i', [-1] * 10)  # 'i' = enteros

    # 🚀 Creamos un proceso que ejecuta la función
    proceso = Process(target=imprimir_contenido_arreglo, args=(arreglo,))

    # ▶️ Iniciamos el proceso
    proceso.start()

    # 🔄 Modificamos el arreglo desde el proceso principal
    for valor in range(10):
        time.sleep(2)
        for indice in range(10):
            arreglo[indice] = valor