import random
with open("ödev3.txt","r+",encoding = "utf-8") as file:
    satirlar = file.readlines()
    secilen_satir = random.sample(satirlar,5)
with open("ödev3_2.txt","w",encoding="utf-8") as file2:
    for satir in secilen_satir:
        file2.write(satir)