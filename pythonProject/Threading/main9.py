"""
- 2 adet thread tanımlayalım.
- Bu threadlerden ilki 3 defa döngü döndürsün. Ardından durulsun.
- Thread2 iki defa ekrana hello world yazdırsın. sonrasında, thread2
- tekrar aktif edilsin ve döngüyü 7 defa daha döndürsün.
- eventlerle tüm threadleri istediğimiz şekilde kontrol etmeliyiz.
- event bağlı olduğu threade göre çalışmaktadır.
"""
import threading

event = threading.Event()
event2 = threading.Event()
def my_function():
    for i in range(0,10):
        if i < 3:
            print(i)
        else:
            event2.set()
            event.wait()
            print(i)


def my_function2():
    event2.wait()
    print("Hello World!")
    print("Hello World!")
    event.set()



threading1 = threading.Thread(target=my_function)
threading2 = threading.Thread(target=my_function2)

threading1.start()
threading2.start()

threading1.join()
threading2.join()
