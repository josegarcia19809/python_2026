import os
import re
from multiprocessing import Pipe
from os.path import join

import time
from multiprocessing.context import Process

REGEX_VIENTO = r"\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*="
REGEX_EXTRAER_VIENTO = r"(\d{5}KT|VRB\d{2}KT)"
REGEX_VIENTO_VARIABLE = r".*VRB\d{2}KT"
REGEX_VIENTO_VALIDO = r"\d{5}KT"
REGEX_SOLO_DIRECCION_VIENTO = r"(\d{3})\d{2}KT"
REGEX_TAF = ".*TAF.*"
REGEX_COMENTARIO = r"\w*#.*"
REGEX_CIERRE_METAR = ".*="


def convertir_a_arreglo(conexion_texto, conexion_metars):
    texto = conexion_texto.recv()

    while texto is not None:
        lineas = texto.splitlines()
        metar_texto = ""
        metars = []

        for linea in lineas:

            if re.search(REGEX_TAF, linea):
                break

            if not re.search(REGEX_COMENTARIO, linea):
                metar_texto += linea.strip()

            if re.search(REGEX_CIERRE_METAR, linea):
                metars.append(metar_texto)
                metar_texto = ""

        conexion_metars.send(metars)
        texto = conexion_texto.recv()

    conexion_metars.send(None)


def extraer_direccion_viento(conexion_metars, conexion_vientos):
    metars = conexion_metars.recv()

    while metars is not None:
        vientos = []

        for metar in metars:

            if re.search(REGEX_VIENTO, metar):

                for token in metar.split():

                    if re.match(REGEX_EXTRAER_VIENTO, token):
                        vientos.append(
                            re.match(REGEX_EXTRAER_VIENTO, token).group(1)
                        )

        conexion_vientos.send(vientos)
        metars = conexion_metars.recv()

    conexion_vientos.send(None)


def calcular_distribucion_viento(conexion_vientos, conexion_distribucion_viento):
    distribucion_viento = [0] * 8

    vientos = conexion_vientos.recv()

    while vientos is not None:

        for viento in vientos:

            if re.search(REGEX_VIENTO_VARIABLE, viento):

                for i in range(8):
                    distribucion_viento[i] += 1

            elif re.search(REGEX_VIENTO_VALIDO, viento):

                direccion = int(
                    re.match(REGEX_SOLO_DIRECCION_VIENTO, viento).group(1)
                )

                indice_direccion = round(direccion / 45.0) % 8

                distribucion_viento[indice_direccion] += 1

        vientos = conexion_vientos.recv()

    conexion_distribucion_viento.send(distribucion_viento)


if __name__ == '__main__':

    conexion_texto_a, conexion_texto_b = Pipe()

    conexion_metars_a, conexion_metars_b = Pipe()

    conexion_vientos_a, conexion_vientos_b = Pipe()

    conexion_distribucion_viento_a, conexion_distribucion_viento_b = Pipe()

    Process(
        target=convertir_a_arreglo,
        args=(conexion_texto_b, conexion_metars_a)
    ).start()

    Process(
        target=extraer_direccion_viento,
        args=(conexion_metars_b, conexion_vientos_a)
    ).start()

    Process(
        target=calcular_distribucion_viento,
        args=(conexion_vientos_b, conexion_distribucion_viento_a)
    ).start()

    ruta_archivos = "metarfiles"

    inicio = time.time()

    for archivo in os.listdir(ruta_archivos):
        f = open(join(ruta_archivos, archivo), "r")

        texto = f.read()

        conexion_texto_a.send(texto)

    conexion_texto_a.send(None)

    distribucion_viento = conexion_distribucion_viento_b.recv()

    fin = time.time()

    print(distribucion_viento)

    print("Tiempo transcurrido:", fin - inicio)
