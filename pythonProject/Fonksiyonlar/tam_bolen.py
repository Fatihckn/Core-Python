def tam_bolen(sayı):
    liste = list()
    for i in range(2,sayı):
        if sayı % i == 0:
            liste.append(i)
    return liste
while True:
    sayı = input("Sayı giriniz:")
    if sayı == "q":
        print("Program sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        print("Sayının tam bölenleri: {}".format(tam_bolen(sayı)))
