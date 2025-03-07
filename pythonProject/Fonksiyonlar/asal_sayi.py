def asal_sayı(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
            else:
                return True
while True:
    sayı = input("Sayı gir:")
    if sayı == "q":
        print("Çıkış yapılıyor")
        break
    else:
        sayı = int(sayı)
        if asal_sayı(sayı):
            print("{} bu sayı asal sayıdır".format(sayı))
        else:
            print("Asal sayı değildir")

