"""
- active_count() metotuyla aktif olan, thread sayısı getirilmektedir.
- Bu metot sonucunda değer int tipinde döndürülecektir.
"""


import threading

def my_function():
    print("Bu bir iş parçacığıdır.")



thread = threading.Thread(target=my_function)
thread.start()


aktif_thread_sayisi = threading.active_count()

print(f"Aktif iş parçacığı sayısı: {aktif_thread_sayisi}")
print(f"Tipi: {type(aktif_thread_sayisi)}")
