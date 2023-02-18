import _thread
import time

def horaActual(nombre_thread, tiempo_espera):
    time.sleep(tiempo_espera)
    print(f"hilo: {nombre_thread} - {time.ctime(time.time())}")


_thread.start_new_thread(horaActual, ("thread_1", 1))
_thread.start_new_thread(horaActual, ("Thread_2", 5))

while True:
    time.sleep(0.1)
