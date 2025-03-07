import os

def txt_dosyalari_bul(klasor_yolu):
    txt_dosyalari = []
    for dosya in os.listdir(klasor_yolu):
        if dosya.endswith(".txt"):
            txt_dosyalari.append(dosya)
    return txt_dosyalari

def dosyalari_dosyaya_yaz(txt_dosyalar, cikti_dosyasi):
    with open(cikti_dosyasi, "w") as dosya:
        for dosya_adi in txt_dosyalar:
            dosya.write(dosya_adi + "\n")

klasor_yolu = "C:\\Users\\cokan\\PycharmProjects\\hafta3_odevler\\For Döngüsü Soruları"  # Klasör yolunu değiştirin
cikti_dosyasi = "ödev9.txt"  # Çıktı dosyasının adını değiştirin

txt_dosyalar = txt_dosyalari_bul(klasor_yolu)
dosyalari_dosyaya_yaz(txt_dosyalar, cikti_dosyasi)

print(f".txt dosyalarının listesi '{cikti_dosyasi}' dosyasına yazıldı.")
