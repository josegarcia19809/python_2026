import time
from threading import Thread, Lock


class AhorradorGastador:
    dinero = 100

    def ahorrador(self):
        for i in range(10000000):
            self.dinero += 10

        print("Ahorrador terminado")

    def gastador(self):
        for i in range(10000000):
            self.dinero -= 10

        print("Gastador terminado")


while True:
    ag = AhorradorGastador()
    Thread(target=ag.ahorrador, args=()).start()
    Thread(target=ag.gastador, args=()).start()
    time.sleep(5)
    print("Dinero al final", ag.dinero)
    print()
    if ag.dinero != 100:
        break
