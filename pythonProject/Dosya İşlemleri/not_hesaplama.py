"""
def not_hesapla(satır):
    satır = satır[:-1] #satır sonundaki \n ifadesini silmek için yaptık

    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    harf_hesapla = (not1 * 0.3) + (not2 * 0.3) + (not3 * 0.4)

    if harf_hesapla >= 90:
        harf = "AA"
    elif harf_hesapla >= 85:
        harf = "BA"
    elif harf_hesapla >= 80:
        harf = "BB"
    elif harf_hesapla >= 75:
        harf = "CB"
    elif harf_hesapla >= 70:
        harf = "CC"
    elif harf_hesapla >= 65:
        harf = "DC"
    elif harf_hesapla >= 60:
        harf = "DD"
    elif harf_hesapla >= 55:
        harf = "FD"
    else:
        harf = "FF"
    if harf_hesapla < 55:
        durum = "k"
    else:
        durum = "g"
    return isim + "------------>" + harf + durum +"\n"
with open("dosya.txt","r",encoding = "utf-8") as file:
    eklenecekler_liste = []
    for i in file:
        eklenecekler_liste.append(not_hesapla(i))
with open("geçenler.txt","w",encoding = "utf-8") as file2:
    for i in eklenecekler_liste:
        if i[-2] == "g":
           file2.write(i)
with open("kalanlar.txt","w",encoding = "utf-8") as file3:
    for i in eklenecekler_liste:
        if i[-2] == "k":
           file3.write(i)

"""
def not_hesapla(satır):
    satır = satır.strip()  # Satır sonundaki boşlukları ve newline karakterini kaldırır

    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    harf_hesapla = (not1 * 0.3) + (not2 * 0.3) + (not3 * 0.4)

    if harf_hesapla >= 90:
        harf = "AA"
    elif harf_hesapla >= 85:
        harf = "BA"
    elif harf_hesapla >= 80:
        harf = "BB"
    elif harf_hesapla >= 75:
        harf = "CB"
    elif harf_hesapla >= 70:
        harf = "CC"
    elif harf_hesapla >= 65:
        harf = "DC"
    elif harf_hesapla >= 60:
        harf = "DD"
    elif harf_hesapla >= 55:
        harf = "FD"
    else:
        harf = "FF"

    # Durumun belirlenmesi
    if harf_hesapla < 55:
        durum = "kaldı"
    else:
        durum = "geçti"

    return f"{isim} ------------> {harf} {durum}\n"

with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler_liste = [not_hesapla(satır) for satır in file]

with open("geçenler.txt", "w", encoding="utf-8") as file2:
    for i in eklenecekler_liste:
        if "geçti" in i:  # Eğer öğrenci geçtiyse
            file2.write(i)

with open("kalanlar.txt", "w", encoding="utf-8") as file3:
    for i in eklenecekler_liste:
        if "kaldı" in i:  # Eğer öğrenci başarısız olduysa
            file3.write(i)

