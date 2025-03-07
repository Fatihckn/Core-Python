def ekok(x,y):
    carpım = 1
    i = 2
    while True:
        if ((x % i == 0) and (y % i == 0)):
            carpım *= i
            x //= i
            y //= i
        elif ((x % i == 0) and (y % i != 0)):
            carpım *= i
            x //= i
        elif ((y % i == 0) and (x % i != 0)):
            carpım *= i
            y //= i
        else:
            i += 1
        if ((x == 1) and (y == 1)):
            break
    return carpım
x = int(input("ilk sayıyı giriniz:"))
y = int(input("ikinci sayıyı giriniz:"))
print("Sayılarının ekoku= ",ekok(x,y))