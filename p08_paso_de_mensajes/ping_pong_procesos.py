from multiprocessing import Process, Pipe
import multiprocessing

import time


def ping(conexion_pipe):
    while True:
        conexion_pipe.send(
            ["Ping", time.time()]
        )

        respuesta_pong = conexion_pipe.recv()

        print(respuesta_pong)

        time.sleep(1)


def pong(conexion_pipe):
    while True:
        mensaje_ping = conexion_pipe.recv()

        print(mensaje_ping)

        time.sleep(1)

        conexion_pipe.send(
            ["Pong", time.time()]
        )


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    extremo_a, extremo_b = Pipe()

    Process(
        target=ping,
        args=(extremo_a,)
    ).start()

    Process(
        target=pong,
        args=(extremo_b,)
    ).start()
