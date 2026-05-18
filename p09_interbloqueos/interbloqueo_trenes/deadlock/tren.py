import random

import time


def mover_tren(tren, distancia, cruces):
    while tren.frente < distancia:

        # 🚂 El tren avanza una unidad
        tren.frente += 1

        # 🛤️ Revisamos todos los cruces
        for cruce in cruces:

            # 🚦 Si el frente del tren llega al cruce,
            # intenta bloquear la intersección
            if tren.frente == cruce.posicion:
                cruce.interseccion.mutex.acquire()
                cruce.interseccion.bloqueado_por = tren.identificador

            # 🚆 Calculamos la parte trasera del tren
            parte_trasera = tren.frente - tren.longitud_tren

            # 🔓 Si el tren ya pasó el cruce,
            # liberamos la intersección
            if parte_trasera == cruce.posicion:
                cruce.interseccion.bloqueado_por = -1
                cruce.interseccion.mutex.release()

        # ⏱️ Pausa pequeña para visualizar la simulación
        time.sleep(0.01)
