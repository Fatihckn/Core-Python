print("""****************************

Python 3. Hafta Ödevi

İçerik:

a)For Döngüsü Soruları
b)While Döngüsü Soruları
c)enumerate() Fonksiyonu Soruları
d)zip() Fonksiyonu Soruları
e)Çıkış için 'e' ye basınız

****************************""")

while True:
    islem = input("Görmek istediğiniz başlığı seçiniz(Çıkış için 'e' tuşlayınız):")
    if islem.lower() == "e":
        print("Çıkış yapılıyor...")
        break
    else:
        if islem.lower() == "a":
            while True:
                try:
                    soru = int(input("Görmek istediğiniz soruyu seçiniz(Çıkış yapmak için '6' giriniz):"))
                except ValueError:
                    print("Geçersiz işlem lütfen tekrar deneyiniz:")
                    continue
                if soru == 1:
                    liste1 = [2,6,10,9,8,4]
                    for i in liste1:
                        print(i)
                elif soru == 2:
                    s = "Fatih"
                    for i in s:
                        print(i)
                elif soru == 3:
                    toplam = 0
                    liste2 = [3,4,8,5,2,1]
                    for i in liste2:
                        toplam += i
                    print(toplam)
                elif soru == 4:
                    for i in range(1,10):
                        print(i ** 2)
                elif soru == 5:
                    sozluk = {"bir":1,"iki":2,"üç":3}
                    for i in sozluk.keys():
                        print(i)
                elif soru == 6:
                    print("For Döngüsü Ödevinden çıkılıyor...")
                    break
                else:
                    print("Geçersiz işlem!!!")
        elif islem.lower() == "b":
            while True:
                try:
                    soru = int(input("Görmek istediğiniz soruyu seçiniz(Çıkış yapmak için '6' giriniz):"))
                except ValueError:
                    print("Geçersiz işlem lütfen tekrar deneyiniz:")
                    continue
                if soru == 1:
                    i = 1
                    while i < 10:
                        print(i)
                        i += 1
                elif soru == 2:

                    while True:
                        try:
                            sayi = int(input("Lütfen bir sayı girin: "))
                            break
                        except ValueError:
                            print("Geçersiz giriş. Lütfen bir sayı girin.")

                    print(f"Girilen sayı: {sayi}")

                elif soru == 3:
                    while True:
                        x = int(input("Bir ile on arasında bir sayı giriniz:"))
                        if x in range(1,10):
                            print(f"Girilen sayının karesi= {x ** 2}")
                            break
                        else:
                            print("Girilen sayı bir ile on arasında değil!!!")

                elif soru == 4:
                    liste3 = [2,5,10,11,43]
                    index = 0
                    while index < len(liste3):
                        eleman = liste3[index]
                        print(eleman)
                        index += 1

                elif soru == 5:
                    liste4 = list(range(1,11))
                    index = 0
                    while index < len(liste4):
                        eleman = liste4[index]
                        if eleman % 2 == 0:
                            print(eleman)
                        index += 1

                elif soru == 6:
                    print("While Döngüsü Ödevinden çıkılıyor...")
                    break
                else:
                    print("Geçersiz işlem!!!")
        elif islem.lower() == "c":
            while True:
                try:
                    soru = int(input("Görmek istediğiniz soruyu seçiniz(Çıkış yapmak için '6' giriniz):"))
                except ValueError:
                    print("Geçersiz işlem lütfen tekrar deneyiniz:")
                    continue
                if soru == 1:
                    liste5 = []
                    eleman = input("Listeye Eleman giriniz (Çıkış için '#' giriniz):")
                    while eleman != '#':
                        liste5.append(eleman)
                        eleman = input("Listeye Eleman giriniz (Çıkış için '#' giriniz):")
                    for index , deger in enumerate(liste5):
                        print(f"İndeksi: {index}, Değeri: {deger}")

                elif soru == 2:
                    s2 = input("Bir string giriniz")
                    for index , deger in enumerate(s2):
                        print(f"İndeksi: {index}, Değeri: {deger}")

                elif soru == 3:
                    liste6 = []
                    eleman = input("Listeye Eleman giriniz (Çıkış için '#' giriniz):")
                    while eleman != '#':
                        liste6.append(eleman)
                        eleman = input("Listeye Eleman giriniz (Çıkış için '#' giriniz):")
                    liste6 = liste6[::-1]
                    for index , deger in enumerate(liste6):
                        print(f"İndeksi: {index}, Değeri: {deger}")

                elif soru == 4:
                    liste7 = []
                    eleman = input("Listeye Sayı giriniz (Çıkış için '#' giriniz):")
                    while eleman != '#':
                        liste7.append(eleman)
                        eleman = input("Listeye Sayı giriniz (Çıkış için '#' giriniz):")
                    for index, deger in enumerate(liste7):
                        deger = int(deger)
                        if deger % 2 == 0 :
                            print(f"{index}.indekste bulunan {deger} değeri çifttir")
                        else:
                            print(f"{index}.indekste bulunan {deger} değeri tektir")

                elif soru == 5:
                    sozluk = {}
                    while True:
                        anahtar = input("Anahtar giriniz(Çıkmak için # giriniz):")
                        if anahtar == '#':
                            print("Çıkış yapılıyor...")
                            break
                        deger = input("Değer giriniz:")
                        sozluk[anahtar] = deger
                    for index, (anahtar, deger) in enumerate(sozluk.items()):
                        print(f"İndeksi: {index},Anahtarı: {anahtar}, Değeri: {deger}")

                elif soru == 6:
                    print("enumerate() fonksiyonu soruları Ödevinden çıkılıyor...")
                    break
                else:
                    print("Geçersiz işlem!!!")
        elif islem.lower() == "d":
            while True:
                try:
                    soru = int(input("Görmek istediğiniz soruyu seçiniz(Çıkış yapmak için '6' giriniz):"))
                except ValueError:
                    print("Geçersiz işlem lütfen tekrar deneyiniz:")
                    continue
                if soru == 1:
                    liste8 = []
                    liste9 = []
                    cıkıs = 1
                    while cıkıs != '#':
                        eleman1 = input("İlk listeye Eleman giriniz:")
                        eleman2 = input("İkinci listeye Eleman giriniz:")
                        liste8.append(eleman1)
                        liste9.append(eleman2)
                        cıkıs = input("Çıkış yapmak istiyorsanız 'Evet', istemiyorsanız herhangi şey tuşlayınız:")
                        if cıkıs == "Evet":
                            cıkıs = '#'
                    for ilk ,iki in zip(liste8,liste9):
                        print(f"ilk liste = {ilk}, ikinci liste = {iki}")

                elif soru == 2:
                    liste10 = []
                    liste11 = []
                    cıkıs = 1
                    while cıkıs != '#':
                        eleman1 = input("İlk listeye Eleman giriniz:")
                        eleman2 = input("İkinci listeye Eleman giriniz:")
                        liste10.append(eleman1)
                        liste11.append(eleman2)
                        cıkıs = input("Çıkış yapmak istiyorsanız 'Evet giriniz':")
                        if cıkıs == "Evet":
                            cıkıs = '#'
                    for ilk ,iki in zip(liste10,liste11):
                        print(f"İki liste sırasıyla toplamları = {ilk + iki}")

                elif soru == 3:
                    liste12 = []
                    liste13 = []
                    cıkıs = 1
                    while cıkıs != '#':
                        eleman1 = input("İlk listeye Eleman giriniz:")
                        eleman2 = input("İkinci listeye Eleman giriniz:")
                        liste12.append(eleman1)
                        liste13.append(eleman2)
                        cıkıs = input("Çıkış yapmak istiyorsanız 'Evet' istemiyorsanız herhangi bir şey tuşlayınız:")
                        if cıkıs == "Evet":
                            cıkıs = '#'

                    birlesik_liste = list(zip(liste12,liste13))
                    print(f"Birleştirilmiş liste = {birlesik_liste}")

                elif soru == 4:
                    liste14 = []
                    string2 = ""
                    while True:
                        kelime = input("Listeye eleman giriniz:")
                        liste14.append(kelime)
                        cıkıs = input("Çıkış yapmak istiyorsanız 'Evet' istemiyorsanız herhangi bir şey tuşlayınız:")
                        if cıkıs == "Evet":
                            break
                    string1 = input("Bir string giriniz:")
                    for x, y in zip(liste14, string1):
                        string2 += str(liste14) + string1
                    print(string2)

                elif soru == 5:
                    liste1 = []
                    liste2 = []
                    liste3 = []
                    flag = 1
                    while True:
                        eleman1 = input("İlk listeye eleman giriniz:")
                        liste1.append(eleman1)
                        eleman2 = input("İkinci listeye eleman giriniz:")
                        liste2.append(eleman2)
                        eleman3 = input("Üçüncü listeye eleman giriniz:")
                        liste3.append(eleman3)
                        cıkıs = input(
                            "Çıkış yapmak istiyorsanız 'Evet' giriniz, istemiyorsanız herhangi bir şey tuşlayınız:")
                        if cıkıs == 'Evet':
                            print("Çıkış yapılıyor")
                            break
                    for x, y, z, in zip(liste1, liste2, liste3):
                        print(f"{flag}.Elemanlarının karşılıklı toplamı = {x + y + z}")
                        flag += 1

                elif soru == 6:
                    print("Zip fonksiyonu soruları ödevinden çıkılıyor...")
                    break
                else:
                    print("Geçersiz işlem!!!")
        else:
            print("Geçersiz İşlem!!!")









