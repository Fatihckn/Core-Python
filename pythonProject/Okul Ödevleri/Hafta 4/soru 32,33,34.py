print("""*****************************

      Listeler İçin Hesaplama Programı

      İşlem Seçiniz:
      1.Soru32
      2.Soru33
      3.Soru34
      Çıkış için '#' Tuşlayınız

*****************************""")


while True:
    try:
        islem = input("Bir İşlem Seçiniz(Çıkış İçin '#' Tuşlayınız):")
        if islem == '#':
            print("Çıkış yapılıyor...")
            break
        islem = int(islem)
    except ValueError:
        print("Geçersiz İşlem! Lütfen bir sayı giriniz.")
        continue
    if islem == 1:
        def kare_al(x):
            return x ** 2
        liste = [1,5,2,6,3,9,8,4,7]
        kareler = list(map(kare_al ,liste))
        print(kareler)
    elif islem == 2:
        liste = [1,5,2,6,3,9,8,4,7]
        kare_al = sorted(map(lambda x:x ** 2 ,liste))
        print(kare_al)
    elif islem == 3:
        def listeolustur():
            bosliste = []

            def push(a):
                bosliste.append(a)
                print(f"yeni liste : {bosliste}")

            def pop():
                if len(bosliste) == 0:
                    print("Liste yok.")
                    return None
                else:
                    sonuc = bosliste.pop()
                    print(f"{sonuc}")

            return {
                'push': push,
                'pop': pop
            }


        liste1 = listeolustur()
        liste1['push'](10)
        liste1['push'](20)
        liste1['push'](30)
        liste1['pop']()
        liste1['pop']()
        liste1['pop']()
    else:
        print("Geçersiz İşlem!!")