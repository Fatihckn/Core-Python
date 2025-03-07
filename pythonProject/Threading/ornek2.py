"""
- Birden fazla web sayfası talep eden ve bunlara paralel olarak request atan ve alınan cevapları bir txt dosyasına kaydeden python kodu.
"""
import threading
import requests


def status_code_kaydet(request_message, url):
    with open('status_code.txt','a') as dosya:
        dosya.write(f"{request_message}->{url}\n")


def get_status_code(url):
    response = requests.get(url)
    status_code_kaydet(response.status_code, url)


web_sayfalari = []
while True:
    kontrol_degiskeni = int(input("İstek atmak için (1), Çıkış yapmak için (-1)"))
    if kontrol_degiskeni == 1:
        web_sayfalari.append(input("Linki girin: "))
    else:
        break

for sayfa in web_sayfalari:
    thread = threading.Thread(target=get_status_code, args=(sayfa,))
    thread.start()



