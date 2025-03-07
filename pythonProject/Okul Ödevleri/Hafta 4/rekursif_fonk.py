def faktoriyel(sayi):
    if sayi == 0:
        return 1
    else:
        return sayi *faktoriyel(sayi-1)

def fibonacci(sayi):
    if sayi <= 1:
       return sayi
    else:
       return fibonacci(sayi - 1) + fibonacci(sayi - 2)

def ackermann(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1,1)
    elif m > 0 and n > 0:
        return ackermann(m-1,ackermann(m,n -1))

def hanoi(n, kaynak_cubuk, hedef_cubuk, yardimci_cubuk):
    if n == 1:
        print(f"{kaynak_cubuk} çubuğundan {hedef_cubuk} çubuğuna disk 1'i taşı.")
        return
    hanoi(n-1, kaynak_cubuk, yardimci_cubuk, hedef_cubuk)
    print(f"{kaynak_cubuk} çubuğundan {hedef_cubuk} çubuğuna disk {n} taşı.")
    hanoi(n-1, yardimci_cubuk, hedef_cubuk, kaynak_cubuk)


import Modulum

print("""*****************************

      Listeler İçin Hesaplama Programı

      İşlem Seçiniz:
      1.Faktoriyel Hesaplama
      2.Fibonacci Hesaplama
      3.Ackermann Hesaplama
      4.Hanoi Hesaplama
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
        sayi = int(input("Bir sayı giriniz:"))
        print(f"Sayının faktoriyeli:",faktoriyel(sayi))
    elif islem == 2:
        sayi = int(input("Bir sayı giriniz:"))
        print(f"Sayının fibonaccisi:",fibonacci(sayi))
    elif islem == 3:
        sayi1 = int(input("Parametrenin ilk sayısını giriniz:"))
        sayi2 = int(input("Parametrenin ikinci sayıyı giriniz:"))
        print(f"({sayi1},{sayi2}) sayılarının ackermannı:",ackermann(sayi1,sayi2))
    elif islem == 4:
        disk_sayisi = 3
        hanoi(disk_sayisi,'A', 'C', 'B')
    else:
        print("Geçersiz İşlem!!")

