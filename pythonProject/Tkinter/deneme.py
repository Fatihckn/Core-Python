def mod(liste):
    maks_tekrar_eden = []
    maks_tekrar_sayısı = 0
    for i in liste:
        tekrar_sayısı = 0
        for x in liste:
            if x == i:
                tekrar_sayısı += 1
        if tekrar_sayısı > maks_tekrar_sayısı:
            maks_tekrar_eden = i 
            maks_tekrar_sayısı = tekrar_sayısı
    return maks_tekrar_eden,maks_tekrar_sayısı



def medyan(liste):
    uzunluk = len(liste)
    liste = sorted(liste)
    if uzunluk % 2 != 0:
        medyan = liste[uzunluk//2]
        return medyan
    else:
        medyan = (liste[uzunluk//2] + liste[(uzunluk//2)-1])/2
        return medyan

def ortalama(liste):
    toplam = 0
    for i in liste:
        toplam += i
    ortalama = toplam / len(liste)
    return ortalama
liste = [12,1,2,3,4,5,3,4]
liste_ortalaması = ortalama(liste)
print(liste_ortalaması)
liste_medyan = medyan(liste)
print(liste_medyan)
liste_maks_tekrar_eden,maks_tekrar_sayisi = mod(liste)
print(f"Dizide en çok tekrar eden sayı: {liste_maks_tekrar_eden}, tekrar sayısı: {maks_tekrar_sayisi}")