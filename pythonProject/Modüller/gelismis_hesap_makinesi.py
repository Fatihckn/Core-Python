import modulum
print("""******************************

Gelişmiş Hesap Makinesi

İşlem Seçiniz:

1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Karekök Alma
6-Üs alma
7-Trigonometrik(sin,cos,tan)
8-Programdan Çıkış

******************************""")

sayı1 = int(input("İlk sayıyı giriniz:"))

while True:

   islem = int(input("İşlem seçiniz:"))

   if (islem == 8):
     print("Hesap Makinesinden çıkılıyor")
     break

   else:
    # sonuc = int(input("Bir sayı giriniz:"))
     if (islem == 1):
       sayı2 = int(input("İkinci sayıyı giriniz:"))
       sayı1 = modulum.toplama(sayı1,sayı2)
       print("İşlem sonucu:",sayı1)
     elif (islem == 2):
       sayı2 = int(input("İkinci sayıyı giriniz:"))
       sayı1 = modulum.cikarma(sayı1,sayı2)
       print("İşlem sonucu:", sayı1)
     elif (islem == 3):
       sayı2 = int(input("İkinci sayıyı giriniz:"))
       sayı1 = modulum.carpma(sayı1,sayı2)
       print("İşlem sonucu:", sayı1)
     elif (islem == 4):
       sayı2 = int(input("İkinci sayıyı giriniz:"))
       if sayı2 == 0:
           print("Bölen '0' olamaz!")
           continue
       sayı1 = modulum.bolme(sayı1,sayı2)
       print("İşlem sonucu:", sayı1)
     elif (islem == 5):
       if sayı1 < 0:
           print("Negatif sayının karekökü alınmaz.")
           continue
       sayı1 = modulum.karekok(sayı1)
       #sayı1 = int(sayı1)
       print("İşlem sonucu:", sayı1)
     elif (islem == 6):
       sayı1 = modulum.us_alma(sayı1)
       print("İşlem sonucu:", sayı1)
     elif (islem == 7):
       sayı2 = input("Fonksiyonu giriniz:")
       sayı1 = modulum.trigonometrik(sayı1,sayı2)
       print("İşlem sonucu:", sayı1)
     else:
         print("Geçersiz işlem!!!")
