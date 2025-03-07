"""
- Event nesnesi oluşturarak olayları belirli bir sırayla gerçekleşmesini
sağlayabiliriz. 
"""
import threading
import time

event = threading.Event()

def my_function():
    print("Thread 1: Çalışmak için bekliyor.")

    event.wait()

    print("Thread 1 aktif edildi.")



def my_function2():
    print("Thread 2: Çalışmaya başladı.")
    time.sleep(2)

    event.set()
    print("Thread 1 , thread2 tarafında aktif edildi.")



thread1 = threading.Thread(target=my_function)
thread2 = threading.Thread(target=my_function2)

thread1.start()
thread2.start()
