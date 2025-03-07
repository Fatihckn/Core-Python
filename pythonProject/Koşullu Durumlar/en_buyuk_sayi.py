print("******************************"
      "Vize Final harf notu hesaplama"
      "******************************")
vize1=int(input("İlk vize notunu giriniz:"))
vize2=int(input("İkinci vize notunu giriniz:"))
final=int(input("final notunu giriniz:"))
harf=(vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
if harf >= 90:
    print("AA")
elif harf >=85:
    print("BA")
elif harf >=80:
    print("BB")
elif harf >=75:
    print("CB")
elif harf >=70:
    print("CC")
elif harf >=65:
    print("DC")
elif harf >=60:
    print("DD")
elif harf >=55:
    print("FD")
else:
    print("FF")