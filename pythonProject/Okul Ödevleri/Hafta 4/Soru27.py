import Modulum
print("""*****************************
      
      Listeler İçin Hesaplama Programı
      
      İşlem Seçiniz:
      1.Ortalama Hesaplama
      2.Medyan Hesaplama
      3.Mod Hesaplama
      4.Standart Sapma Bulma
      5.Varyant Bulma
      Çıkış için '#' Tuşlayınız
      
*****************************""")
liste = []
islem = None
deger = input("Listeye Eleman Giriniz (Çıkış İçin # Tuşlayınız):")

while deger != '#':
    try:
        deger = int(deger)
        liste.append(deger)
        deger = input("Listeye Eleman Giriniz (Çıkış İçin # Tuşlayınız):")
    except ValueError:
        print("Geçersiz işlem! Lütfen bir sayı giriniz.")
        deger = input("Listeye Eleman Giriniz (Çıkış İçin # Tuşlayınız):")

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
            print("Listenizin Ortalaması:",Modulum.ortalama_hesaplama(liste))
      elif islem == 2:
            print("Listenizin Medyanı:", Modulum.medyan_hesaplama(liste))
      elif islem == 3:
            tekrar_sayisi , sayi = Modulum.mod_hesaplama(liste)
            print(f"Listenizde en çok tekrar eden sayı:{sayi} Kaç kez tekrar ettiği:{tekrar_sayisi}")
      elif islem == 4:
            print("Listenizin Standar Sapması:", Modulum.standart_sapma(liste))
      elif islem == 5:
            print("Listenizin Varyansı:", Modulum.varyans_hesaplama(liste))
      else:
            print("Geçersiz İşlem!!")





