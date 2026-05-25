import time


# 🔒 Bloquea todas las intersecciones necesarias
# dentro de un rango de distancia
def bloquear_intersecciones_en_distancia(identificador, inicio_reserva,
                                         fin_reserva, cruces):
    intersecciones_a_bloquear = []

    # 🛤️ Revisamos todos los cruces
    for cruce in cruces:
        # 🚦 Verificamos si el cruce está dentro
        # del rango reservado
        if (
                fin_reserva >= cruce.posicion >= inicio_reserva
                and cruce.interseccion.bloqueado_por != identificador
        ):
            intersecciones_a_bloquear.append(
                cruce.interseccion
            )

    # 📋 Ordenamos las intersecciones por ID
    intersecciones_a_bloquear = sorted(
        intersecciones_a_bloquear,
        key=lambda interseccion: interseccion.identificador
    )

    # 🔒 Bloqueamos cada intersección
    for interseccion in intersecciones_a_bloquear:
        interseccion.mutex.acquire()
        interseccion.bloqueado_por = identificador

        # ⏱️ Pequeña pausa para la simulación
        time.sleep(0.01)


# 🚂 Movimiento principal del tren
def mover_tren(tren, distancia, cruces):
    while tren.frente < distancia:

        # 🚂 El tren avanza
        tren.frente += 1

        # 🛤️ Revisamos todos los cruces
        for cruce in cruces:

            # 🚦 Cuando el tren llega al cruce
            if tren.frente == cruce.posicion:
                bloquear_intersecciones_en_distancia(
                    tren.identificador,
                    cruce.posicion,
                    cruce.posicion + tren.longitud_tren,
                    cruces
                )

            # 🚆 Calculamos la parte trasera
            parte_trasera = (
                    tren.frente - tren.longitud_tren
            )

            # 🔓 Si el tren ya pasó el cruce,
            # liberamos la intersección
            if parte_trasera == cruce.posicion:
                cruce.interseccion.bloqueado_por = -1
                cruce.interseccion.mutex.release()

        # ⏱️ Pausa para visualizar la animación
        time.sleep(0.01)
