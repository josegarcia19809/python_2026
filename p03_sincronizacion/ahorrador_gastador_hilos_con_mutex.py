import time
from threading import Thread, Lock


class AhorradorGastador:
    dinero = 100
    mutex = Lock()

    def ahorrador(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.dinero += 10
            self.mutex.release()
        print("Ahorrador terminado")

    def gastador(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.dinero -= 10
            self.mutex.release()
        print("Gastador terminado")


ag = AhorradorGastador()
Thread(target=ag.ahorrador, args=()).start()
Thread(target=ag.gastador, args=()).start()
time.sleep(5)
print("Dinero al final", ag.dinero)
print("-" * 100)
