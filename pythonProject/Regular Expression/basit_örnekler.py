import re

s = "bugün hava çok güzel"

a = re.findall("[a-d]",s) #[a,b,c,ç,d] yaparsak türkeç olan karakterleri gösterir
print(a)

a = re.findall("h..a",s)
print(a)

a = re.search("h..a",s) #karakterin 6 ile 10. indekste ve bulunduğunu söyler
print(a)

a = re.findall("^bugün",s)
print(a)

a = re.findall("okx*",s)
print(a)

a = re.split("a",s) #a harfine göre ayırdı
print(a)

a = re.sub(" ","*",s) #istediğimiz bir karakteri istediğimiz bir karakterle değişirir
print(a)

a = re.sub("çok","pek",s)
print(a)

a = re.sub("h..a","ders",s)
print(a)

pattern = r"test" #bir dizeyi "r" öneki ile başlatarak, Python'a bu dizenin tam olarak olduğu gibi işlenmesini söylersiniz, yani kaçış dizilerini görmezden gelir.
text = "Bu bir test metnidir."

if re.search(pattern,text):
    print("Eşleşme bulundu")
else:
    print("Eşleşme bulunamadadı")

text = "E-posta adresim info@example.com."
match = re.search(r"(\w+)@(\w+\.\w+)",text)
if match:
    print("E-posta adresi: ",match.group())
    print("Kulalnıcı adı: ", match.group(1))
    print("Alan adı: ",match.group(2))

text = """Bana info@example.com adresinden ulaşabilirsiniz. Ayrıca,
admin@test.com adresinden de bize ulaşabilirsiniz"""
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",text)
print(emails)

text = "Benim telefon numaram: 555-123-4567. Diğer telefon numaram: (555) 987-6543."
phone_numbers = re.findall(r"\b(?:\d{3}[-\.\s]|\(\d{3}\))\d{3}[-\.\s]\d{4}\b", text)
formatted_numbers = [re.sub(r"\D", "", number) for number in phone_numbers]
print(formatted_numbers)

html_text = "<p>Bu bir <strong>HTML</strong> metnidir.</p><a href='example.com'>Bağlantı</a>"
clean_text = re.sub(r"<[^>]+>", "", html_text)
print(clean_text) # Çıktı: Bu bir HTML metnidir.Bağlantı

file_paths = [

  "/home/user/documents/file1.txt",

  "/home/user/images/picture.jpg",

  "/var/www/html/index.html",

  "/home/user/downloads/document.pdf"

]

for path in file_paths:

  match = re.search("/([^/]+)\.(\w+)$", path)

  if match:

    filename = match.group(1)

    extension = match.group(2)

    print("Dosya Adı:", filename)

    print("Uzantı:", extension)


text = "IP adresleri: 192.168.1.1, 10.0.0.1 ve 172.16.0.1."

ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)

print(ip_addresses)