import time
from threading import Thread  # Importamos la clase Thread para crear hilos

def hacer_trabajo():
   print("Iniciando trabajo")  # Mensaje cuando el hilo comienza
   time.sleep(1)  # Simula una tarea que tarda 1 segundo
   print("Trabajo terminado")  # Mensaje cuando el hilo finaliza


# Creamos 5 hilos que ejecutan la misma función
for _ in range(5):
   hilo = Thread(target=hacer_trabajo, args=())  # Creamos el hilo
   hilo.start()  # Iniciamos la ejecución del hilo