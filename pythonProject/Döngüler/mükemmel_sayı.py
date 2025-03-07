print("******************************\n"
      "Mükemmel sayı bulma programı\n"
      "******************************\n")
toplam = 0
i = 1
sayı = int(input("Sayı Giriniz:"))
while(sayı > i):
    if (sayı % i == 0):
        toplam += i
        i += 1
    else:
        i += 1
if toplam == sayı:
    print("Bu sayı mükemmel sayıdır.")
else:
    print("Bu sayı mükemmel sayı değildir.")