"""
- Şu anda aktif olan threadleri görmek için enumerate() kullanılmalıdır.
- MainThread, Thread1 ve Thread2 olarak 3 adet threade sahibiz.
- enumerate() ile gelen threadlerin sayısı ile active_count() aynı olmalıdır.

"""
import threading
import time

def my_function():
    print("Bu bir örnek iş parçacığıdır.")
    time.sleep(2)


def my_function2():
    print("Bu bir örnek iş parçacığıdır.")
    time.sleep(2)


thread1 = threading.Thread(target=my_function)
thread1.start()



thread2 = threading.Thread(target=my_function)
thread2.start()



threads = threading.enumerate()
print("Şu anda çalışan iş parçacıkları")
for thread in threads:
    print(thread.name)

print(threading.active_count())


