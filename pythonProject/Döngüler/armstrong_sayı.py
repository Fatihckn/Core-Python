print("******************************\n"
      "Armstrong sayı bulma programı\n"
      "******************************")
toplam = 0
basamak = 0
sayı = input("Sayı:")
basamak_sayısı = len(sayı)
sayı = int(sayı)
geçici_sayi = sayı

while (geçici_sayi > 0):
    basamak = geçici_sayi % 10
    toplam += basamak ** basamak_sayısı
    geçici_sayi //= 10

if toplam == sayı:
    print("Armstrong sayıdır.")
else:
    print("Armstrong sayı değildir.")