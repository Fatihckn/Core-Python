"""
- Bu kodda 2 döngünün paralel olarak devam ettiğini çıktıda görebiliriz.
- time sleep vererek adım adım görebiliriz.
"""



import threading
import time

def my_function():
    count = 0
    while True:
        print(count)
        count = count + 1
        time.sleep(1)


def my_function2():
    count = 10
    while True:
        print(count)
        count = count + 1
        time.sleep(1)

thread1 = threading.Thread(target=my_function)
thread1.start()


thread2 = threading.Thread(target=my_function2)
thread2.start()
