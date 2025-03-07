print("*************************************\n"
      "Faktoriyel bulma programı\n"
      "Çıkmak için 'q'ya basınız\n"
      "*************************************")
while True:
    sayı = input("Sayı giriniz:")
    if sayı == "q":
        print("Programdan çıkılıyor...")
        break
    else:
        sayı = int(sayı)
        faktoriyel = 1
        for i in range(2,sayı+1):
            faktoriyel *= i
        print("Sayının faktoriyeli: {}".format(faktoriyel))

