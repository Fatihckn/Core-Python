import math
def toplama(x,y):
    return x + y

def cikarma(x,y):
    return x - y

def bolme(x,y):
    return x / y

def carpma(x,y):
    return x * y

def karekok(x):
    return math.sqrt(x)

def us_alma(x):
    return x ** 2

def trigonometrik(derece,fonk):
    radyan = math.radians(derece)
    if (fonk == "sin"):
        return math.sin(radyan)
    elif (fonk == "cos"):
        return math.cos(radyan)
    elif (fonk == "tan"):
        return math.tan(radyan)
    else:
        print("Geçersiz fonksiyon")