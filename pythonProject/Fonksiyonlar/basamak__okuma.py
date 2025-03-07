birler = ["","bir","İki","Üç","Dört","Beş","altı","yedi","sekiz","dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
def okuma(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    return onlar[ikinci]+" "+birler[birinci]

sayı = int(input("Bir sayı giriniz:"))
print(okuma(sayı))