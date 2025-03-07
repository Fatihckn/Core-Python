def ortalama_hesaplama(list):
    toplam = 0
    for i in list:
        toplam += i
    uzunluk = len(list)
    ortalama = toplam / uzunluk
    return ortalama

def medyan_hesaplama(list):
    uzunluk = len(list)
    sıralı = sorted(list)
    if uzunluk % 2 == 0:
        medyan = (list[uzunluk // 2] + list[(uzunluk // 2)-1])//2
        return medyan
    else:
        medyan = list[(uzunluk // 2)]
        return medyan

def mod_hesaplama(list):
    en_cok_tekrar_eden = None
    en_cok_tekrar_sayisi = 0
    for i in list:
        tekrar_sayisi = 0
        for x in list:
            if x == i:
                tekrar_sayisi += 1
        if tekrar_sayisi > en_cok_tekrar_sayisi:
            en_cok_tekrar_eden = i
            en_cok_tekrar_sayisi = tekrar_sayisi
    return en_cok_tekrar_sayisi,en_cok_tekrar_eden

def standart_sapma(list):
    toplam = 0
    temp = 0
    for i in list:
        toplam += i
    ortalama = toplam / len(list)
    for i in list:
        temp += (i - ortalama)**2
    varyans = temp / (len(list))
    standart_sapmma = varyans ** 0.5
    return standart_sapmma

def varyans_hesaplama(list):
    toplam = 0
    temp = 0
    for i in list:
        toplam += i
    ortalama = toplam / len(list)
    for i in list:
        temp += (i - ortalama)**2
    varyans = temp / (len(list))
    return varyans



