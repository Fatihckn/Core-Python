def kelime_sayisi(dosya_adi, aranan):
    with open(dosya_adi, "r", encoding="utf-8") as file:
        tekrar_sayisi = 0
        for satir in file:
            kelimeler = satir.split()
            for kelime in kelimeler:
                if kelime == aranan:
                    tekrar_sayisi += 1
        return tekrar_sayisi

dosya_ismi = "ödev2.txt"
aranan_kelime = "Çokan"
tekrar_sayisi = kelime_sayisi(dosya_ismi, aranan_kelime)
print(f"{aranan_kelime} Kelimesinin tekrar sayısı: {tekrar_sayisi}")
