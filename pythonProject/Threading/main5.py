"""
- threading.main_thrad() metotu ile ana thread döndürülür.
- başka bir thread başlatılsa bile yine de ana thread aynıdır.
"""


import threading
import time


def my_function():
    print("Bu bir örnek iş parçacığıdır.")
    time.sleep(2)


ana_thread = threading.main_thread()
print("Ana iş parçacığı: ",ana_thread)


thread = threading.Thread(target=my_function)
thread.start()

print("Ana iş parçacığı: ",ana_thread)
