print("*****************************"
      "Beden kitle endeksi hesaplama"
      "*****************************")
boy=float(input("Boyunuzu giriniz:"))
kilo=float(input("Kilonuzu giriniz:"))
bki= (kilo / (boy * boy))
if bki < 18.5:
    print("Zayıfsınız.")
elif bki < 25:
    print("Normalsiniz.")
elif bki < 30:
    print("Fazla kilolusunuz.")
else:
    print("Obezsiniz.")