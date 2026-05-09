import os
import re
from os.path import join

import time

REGEX_VIENTO = r"\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*="
REGEX_EXTRAER_VIENTO = r"(\d{5}KT|VRB\d{2}KT)"
REGEX_VIENTO_VARIABLE = r".*VRB\d{2}KT"
REGEX_VIENTO_VALIDO = r"\d{5}KT"
REGEX_SOLO_DIRECCION_VIENTO = r"(\d{3})\d{2}KT"
REGEX_TAF = r".*TAF.*"
REGEX_COMENTARIO = r"\w*#.*"
REGEX_CIERRE_METAR = r".*="


def convertir_a_arreglo(texto):
    lineas = texto.splitlines()

    cadena_metar = ""

    metars = []

    for linea in lineas:

        if re.search(REGEX_TAF, linea):
            break

        if not re.search(REGEX_COMENTARIO, linea):
            cadena_metar += linea.strip()

        if re.search(REGEX_CIERRE_METAR, linea):
            metars.append(cadena_metar)
            cadena_metar = ""

    return metars


def extraer_direccion_viento(metars):
    vientos = []

    for metar in metars:

        if re.search(REGEX_VIENTO, metar):

            for token in metar.split():

                if re.match(REGEX_EXTRAER_VIENTO, token):
                    vientos.append(
                        re.match(REGEX_EXTRAER_VIENTO, token).group(1)
                    )

    return vientos


def minar_distribucion_viento(vientos, distribucion_viento):
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

    return distribucion_viento


if __name__ == '__main__':
    ruta_archivos = "metarfiles"
    distribucion_viento = [0] * 8
    inicio = time.time()

    for archivo in os.listdir(ruta_archivos):
        f = open(join(ruta_archivos, archivo), "r")
        texto = f.read()
        metars = convertir_a_arreglo(texto)
        vientos = extraer_direccion_viento(metars)
        distribucion_viento = minar_distribucion_viento(
            vientos,
            distribucion_viento
        )

    fin = time.time()
    print(distribucion_viento)
    print("Tiempo transcurrido", fin - inicio)
