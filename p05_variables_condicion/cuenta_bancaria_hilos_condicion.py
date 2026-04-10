import time
from threading import Thread, Condition


class AhorradorGastador:
    dinero = 100
    cv = Condition()

    def ahorrador(self):
        for i in range(1000000):
            self.cv.acquire()
            self.dinero += 10
            self.cv.notify()
            self.cv.release()
        print("Ahorrador terminado")

    def gastador(self):
        for i in range(500000):
            self.cv.acquire()
            while self.dinero < 20:
                self.cv.wait()
            self.dinero -= 20
            if self.dinero < 0:
                print("Dinero en el banco", self.dinero)
            self.cv.release()
        print("Gastador terminado")


ag = AhorradorGastador()
Thread(target=ag.ahorrador, args=()).start()
Thread(target=ag.gastador, args=()).start()
time.sleep(5)
print("Dinero al final", ag.dinero)
