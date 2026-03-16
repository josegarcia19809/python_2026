import json
import urllib.request
import time
from threading import Thread, Lock

contador_finalizados = 0


def contar_letras(url, frecuencias, mutex):
    respuesta = urllib.request.urlopen(url)
    texto = str(respuesta.read())
    mutex.acquire()
    for caracter in texto:
        letra = caracter.lower()
        if letra in frecuencias:
            frecuencias[letra] += 1

    global contador_finalizados
    contador_finalizados += 1
    mutex.release()


def main():
    frecuencias = {}
    mutex = Lock()
    for letra in "abcdefghijklmnopqrstuvwxyz":
        frecuencias[letra] = 0

    inicio = time.time()

    for i in range(1000, 1020):
        thread = Thread(target=contar_letras,
                        args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frecuencias,
                              mutex))
        thread.start()
    while True:
        mutex.acquire()
        if contador_finalizados == 20:
            break
        mutex.release()
        time.sleep(0.5)

    fin = time.time()

    print(json.dumps(frecuencias, indent=4))
    print("Terminado, tiempo empleado:", fin - inicio)


main()
