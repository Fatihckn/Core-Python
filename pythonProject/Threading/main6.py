"""
- Bir değeri bir thread kullanacaksa o değişkene diğer threadlerin
engellemek için lock.acqurie() ile değişkeni threadin üstüne alıyoruz.
ardından lock.release() ile serbest bırakılacak ve diğer thread
kullanılacak.
"""

import threading


# Lock objesi oluşturuldu.
lock = threading.Lock()

miktar = 0

def ekleme_yap():
    global miktar
    lock.acquire()
    try:
        miktar += 1
    finally:
       lock.release()


thread1 = threading.Thread(target=ekleme_yap)
thread1.start()

thread2 = threading.Thread(target=ekleme_yap)
thread2.start()

print("Miktar: ",miktar)
