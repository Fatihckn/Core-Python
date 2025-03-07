import random
import time

class Kumanda():

    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon kapatılıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi azaltmak için: '<'\nSesi arttırmak için: '>' Giriniz.\nÇıkış: çıkış ")

            if cevap == '>':
                if  self.tv_ses == 31:
                    print("Ses en yüksekte daha fazla arttırılamaz")
                else:
                    print("Ses arttırılıyor...")
                    self.tv_ses += 1
            elif cevap == '<':
                if self.tv_ses == 0:
                    print("Ses en kısıkta daha fazla azaltılamaz")
                else:
                    print("Ses arttırılıyor...")
                    self.tv_ses -= 1
            elif cevap == "çıkış":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz işlem, lütfen geçerli bir işlem giriniz")

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print(f"Şu anki kanal: {self.kanal}")

    def kanal_silme(self,kanal_silme):
        self.kanal_listesi.remove(kanal_silme)
        print("Kanal silindi")

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return f"Tv Durumu: {self.tv_durum}\nKanal Listesi: {self.kanal_listesi}\nMevcut Kanal: {self.kanal}"

print("""
Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısı Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için '9'e Tuşlayınız



""")
kumanda = Kumanda()
islem = 0

while True:
    try:
        islem = int(input("İşlem giriniz(Çıkmak için '9'e Tuşlayınız): "))
    except ValueError:
        print("Geçersiz İşlem! Lütfen tekrar deneyiniz")
        continue
    if islem == 1:
        kumanda.tv_ac()
    elif islem == 2:
        kumanda.tv_kapat()
    elif islem == 2:
        kumanda.tv_kapat()
    elif islem == 3:
        kumanda.ses_ayarlari()
    elif islem == 4:
        eklenecek_kanal = input("Kanal isimlerini ',' ile ayırarak giriniz: ")
        eklenecek_kanal = eklenecek_kanal.split(",")
        for i in eklenecek_kanal:
            kumanda.kanal_ekle(i)
    elif islem == 5:
        print("Kanal sayısı: ",len(kumanda))
    elif islem == 6:
        kumanda.rastgele_kanal()
    elif islem == 7:
        print(kumanda)
    elif islem == 8:
        if kumanda.kanal_listesi == []:
            print("Hiç kanal bulunmamaktadır")
        else:
            kanal_sil = input(f"Bu kanallar bulunmaktadır: {kumanda.kanal_listesi}\nSilmek istediğiniz kanalı giriniz:")
            if kanal_sil in kumanda.kanal_listesi:
                kumanda.kanal_silme(kanal_sil)
            else:
                print("Aradığınız kanal bulunmamaktadır.")
                continue

    elif islem == 9:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem! Lütfen tekrar giriniz")
        continue