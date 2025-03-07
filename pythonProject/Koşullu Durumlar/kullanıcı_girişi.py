print("******************************"
      "Kullanıcı girişi"
      "******************************")
ad=input("Kullanıcı Adı:")
parola=int(input("Parola:"))
if ad == "Fatih" and parola == 1234:
    print("Hoşgeldiniz.")
elif ad != "Fatih" and parola == 1234:
    print("Yanlış Ad")
elif ad == "Fatih" and parola != 1234:
    print("Yanlış parola")
else:
    print("yanlış ad ve parola")
