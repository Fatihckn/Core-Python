print("*******************************\n"
      ""
      "Atm Makinesine Hoşgeldiniz\n"
      ""
      "İşlemler:\n"
      ""
      "1.Bakiye Sorgulama\n"
      "2.Para Çekme\n"
      "3.Para Yatırma\n"
      "Programdan çıkmak için 'q'ya basınız\n"
      "*******************************")
bakiye = 1000
while True:
    islem = input("İşlem giriniz:")
    if islem == "q":
        print("Program sonlanıyor...")
        break
    elif islem == "1":
        print("Bakiyeniz: {}".format(bakiye))
    elif islem == "2":
        tutar = int(input("Çekmek istediğiniz tutarı giriniz:"))
        if tutar > bakiye:
            print("Yetersiz bakiye.")
        else:
            bakiye -= tutar
            print("Yeni bakiyeniz: {}".format(bakiye))
    elif islem == "3":
        tutar = int(input("Yatırmak istediğiniz tutarı giriniz:"))
        bakiye += tutar
        print("Yeni bakiyeniz: {}".format(bakiye))
    else:
        print("Geçersiz işlem!!")