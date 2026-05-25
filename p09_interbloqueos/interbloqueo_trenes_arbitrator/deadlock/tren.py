import threading
import time

# 🧑‍⚖️ Variable de condición que actuará
# como controlador/arbitrador
controlador = threading.Condition()


# ✅ Verifica si todas las intersecciones están libres
def todas_libres(intersecciones_a_bloquear):
    for interseccion in intersecciones_a_bloquear:
        # 🚦 Si alguna intersección está ocupada
        if interseccion.bloqueado_por >= 0:
            return False

    return True


# 🔒 Bloquea las intersecciones necesarias
# dentro de una distancia determinada
def bloquear_intersecciones_en_distancia(
        identificador,
        inicio_reserva,
        fin_reserva,
        cruces
):

    intersecciones_a_bloquear = []

    # 🛤️ Revisamos todos los cruces
    for cruce in cruces:

        # 🚦 Verificamos si el cruce está dentro
        # del rango reservado
        if (
            fin_reserva >= cruce.posicion >= inicio_reserva
            and cruce.interseccion.bloqueado_por != identificador
        ):
            intersecciones_a_bloquear.append(                cruce.interseccion            )

    # 🔐 Bloqueamos el controlador
    controlador.acquire()

    # ⏳ Mientras alguna intersección esté ocupada
    while not todas_libres(intersecciones_a_bloquear):
        # 😴 El hilo espera
        controlador.wait()

    # 🚦 Marcamos todas las intersecciones como ocupadas por este tren
    for interseccion in intersecciones_a_bloquear:
        interseccion.bloqueado_por = identificador
        # ⏱️ Pequeña pausa para visualizar
        time.sleep(0.01)

    # 🔓 Liberamos el controlador
    controlador.release()


# 🚂 Movimiento principal del tren
def mover_tren(tren, distancia, cruces):
    while tren.frente < distancia:
        # 🚂 El tren avanza una unidad
        tren.frente += 1

        # 🛤️ Revisamos todos los cruces
        for cruce in cruces:
            # 🚦 Si el tren llega al cruce
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

            # 🔓 Si el tren ya pasó el cruce
            if parte_trasera == cruce.posicion:
                # 🔐 Bloqueamos el controlador
                controlador.acquire()

                # 🚦 Marcamos la intersección
                # como libre
                cruce.interseccion.bloqueado_por = -1

                # 📢 Avisamos a todos los hilos
                controlador.notify_all()

                # 🔓 Liberamos el controlador
                controlador.release()

        # ⏱️ Pausa para visualizar
        time.sleep(0.01)