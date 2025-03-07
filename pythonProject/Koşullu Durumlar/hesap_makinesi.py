print("Hesap Makinesine Hoşgeldiniz...")
a=float(input("İlk sayıyı giriniz:"))
b=float(input("İkinci sayıyı giriniz:"))
islem=input("İşlem giriniz:")
if islem == "+":
    print("İşlem sonucu = {}".format(a+b))
elif islem == "-":
    print("İşlem sonucu = {}".format(a-b))
elif islem == "/":
    print("İşlem sonucu = {}".format(a/b))
elif islem == "*":
    print("İşlem sonucu = {}".format(a*b))
else:
    print("Geçersiz işlem!!")


