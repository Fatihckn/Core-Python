import csv
with open("ödev4.csv","w",encoding = "utf-8", newline='') as csvfile:
    fieldnames = ['İsim', 'Soyisim', 'Yaş']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'İsim': 'Ahmet', 'Soyisim': 'Yılmaz', 'Yaş': 30})
    writer.writerow({'İsim': 'Ayşe', 'Soyisim': 'Kaya', 'Yaş': 25})
    writer.writerow({'İsim': 'Mehmet', 'Soyisim': 'Demir', 'Yaş': 35})
    writer.writerow({'İsim': 'Fatma', 'Soyisim': 'Çelik', 'Yaş': 28})

with open("ödev4.csv","r",encoding="utf-8",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    sıralanmış_veri = sorted(reader, key=lambda row:row['İsim'])

with open("ödev5.csv","w",encoding="utf-8",newline='') as csvfile:
    fieldnames = ['İsim', 'Soyisim', 'Yaş']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    for row in sıralanmış_veri:
        writer.writerow(row)
