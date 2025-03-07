def ebob(x,y):
    i = 1
    ebob = 1
    while( i <= x and i <= y):
        if (( x % i == 0 ) and ( y % i == 0 ) ):
            ebob = i
        i += 1
    return ebob

x = int(input("İlk sayıyı giriniz:"))
y = int(input("İkinci sayıyı giriniz:"))
print("Bu iki sayının ebobu: ",ebob(x,y))