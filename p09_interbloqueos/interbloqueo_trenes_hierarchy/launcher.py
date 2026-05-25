from threading import Lock, Thread

from deadlock.tren import *
from draw_trains import *
from modelos import *

# 📏 Longitud de todos los trenes
longitud_tren = 200


def principal():

    # 🖥️ Creamos la ventana de la simulación
    ventana = GraphWin('Trenes en una caja', 800, 800)
    ventana.setBackground('black')

    # 🚂 Clase encargada de dibujar los trenes
    animacion_trenes = AnimacionTrenes(ventana, longitud_tren)

    # 📋 Listas de trenes e intersecciones
    trenes = []
    intersecciones = []

    # 🚂 Creamos 4 trenes
    for i in range(4):
        trenes.append(Tren(i, longitud_tren, 0))

    # 🚦 Creamos 4 intersecciones con mutex
    for i in range(4):
        intersecciones.append(
            Interseccion(i, Lock(), -1)
        )

    # 🧵 Hilo del tren 1
    hilo1 = Thread(
        target=mover_tren,
        args=(
            trenes[0],
            780,
            [
                Cruce(320, intersecciones[0]),
                Cruce(460, intersecciones[1])
            ]
        )
    )

    # 🧵 Hilo del tren 2
    hilo2 = Thread(
        target=mover_tren,
        args=(
            trenes[1],
            780,
            [
                Cruce(320, intersecciones[1]),
                Cruce(460, intersecciones[2])
            ]
        )
    )

    # 🧵 Hilo del tren 3
    hilo3 = Thread(
        target=mover_tren,
        args=(
            trenes[2],
            780,
            [
                Cruce(320, intersecciones[2]),
                Cruce(460, intersecciones[3])
            ]
        )
    )

    # 🧵 Hilo del tren 4
    hilo4 = Thread(
        target=mover_tren,
        args=(
            trenes[3],
            780,
            [
                Cruce(320, intersecciones[3]),
                Cruce(460, intersecciones[0])
            ]
        )
    )

    # ▶️ Iniciamos todos los hilos
    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()

    # 🔄 Actualizamos constantemente la animación
    while True:
        animacion_trenes.actualizar_trenes(trenes, intersecciones)
        time.sleep(0.01)


# 🚀 Ejecutamos el programa
principal()