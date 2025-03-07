"""
- Kullanıcıdan isim ve soyisim alırız. Bunları ayrı ayrı 2 thread'e vererek isimler ve soyisimler farklı dosyalara kaydedildi.
- Dosyaya kaydetme işi threading operasyonu ile yapıldı.


"""


import threading
import time
event1 = threading.Event()
event2 = threading.Event()

def ismi_kaydet(isim):
    event1.wait()
    with open('isimler.txt','a') as dosya:
        dosya.write(f"{isim}\n")
    
    event1.wait()
    time.sleep(1)

def soyismi_kaydet(soyisim):
    event2.wait()
    with open('soyisim.txt','a') as dosya:
        dosya.write(f"{soyisim}\n")
    
    event2.wait()
    time.sleep(1)

def bilgileri_al():
    while True:
        isim = input("İsminizi girin: ")
        soyisim = input("Soyisminizi girin: ")
    
        isim_kaydet_thread = threading.Thread(target=ismi_kaydet, args=(isim,))
        soyisim_kaydet_thread = threading.Thread(target=soyismi_kaydet, args=(soyisim,))

        event1.set()
        event2.set()

        isim_kaydet_thread.start()
        soyisim_kaydet_thread.start()


bilgileri_al()










