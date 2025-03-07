print("*************************"
      "Geometrik şekil hesaplama"
      "*************************")
sekil=input("Hangi şekili bulmak istiyorsunuz:")
if sekil == "Dörtgen":
    a = int(input("ilk kenar:"))
    b = int(input("ikinci kenar:"))
    c = int(input("üçüncü kenar:"))
    d = int(input("dördüncü kenar:"))
    if ((abs(a) == abs(b)) and (abs(a) == abs(c)) and (abs(a) == abs(d))):
        print("Karedir.")
    elif ((abs(a) == abs(c)) and (abs(b) == abs(d))):
        print("Dikdörtgendir.")
    elif ((abs(a) == abs(b)) and (abs(c) == abs(d))):
        print("Dikdörtgendir.")
    elif ((abs(a) == abs(d)) and (abs(b) == abs(c))):
        print("Dikdörtgendir.")
    else:
        print("Dörtgendir.")
elif sekil == "Üçgen":
    a=int(input("İlk kenarı giriniz:"))
    b=int(input("İkinci kenarı giriniz:"))
    c=int(input("Üçüncü kenarı giriniz:"))
    if ((abs(a+b) > c) and (abs(a+c) > b) and (abs(b+c) > a)):
        if ((a == b) and (a == c)):
            print("Eşkenar üçgen.")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar üçgen.")
        else:
            print("Çeşitkenar Üçgen.")
    else:
        print("Üçgen belirtmiyor.")
else:
    print("Geçersiz şelil!!")