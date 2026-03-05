import multiprocessing

from multiprocessing import Process


def hacer_trabajo():
    print("Iniciando trabajo")
    contador = 0
    for _ in range(20000000):
        contador += 1
    print("Trabajo terminado")


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    for _ in range(5):
        proceso = Process(target=hacer_trabajo, args=())
        proceso.start()