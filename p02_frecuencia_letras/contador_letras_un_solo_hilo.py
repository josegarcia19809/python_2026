import json
import urllib.request
import time


def contar_letras(url, frecuencias):
    respuesta = urllib.request.urlopen(url)
    texto = str(respuesta.read())
    for caracter in texto:
        letra = caracter.lower()
        if letra in frecuencias:
            frecuencias[letra] += 1


def main():
    frecuencias = {}
    for letra in "abcdefghijklmnopqrstuvwxyz":
        frecuencias[letra] = 0

    inicio = time.time()

    for i in range(1000, 1020):
        contar_letras(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frecuencias)

    fin = time.time()

    print(json.dumps(frecuencias, indent=4))
    print("Terminado, tiempo empleado:", fin - inicio)


main()