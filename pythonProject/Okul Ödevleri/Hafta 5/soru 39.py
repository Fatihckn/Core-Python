import json


veri = [
    {"İsim": "Ahmet", "Soyisim": "Yılmaz", "Yaş": 30},
    {"İsim": "Ayşe", "Soyisim": "Kaya", "Yaş": 25},
    {"İsim": "Mehmet", "Soyisim": "Demir", "Yaş": 35},
    {"İsim": "Fatma", "Soyisim": "Çelik", "Yaş": 28}
]

with open("ödev6.json","w",encoding = "utf-8") as file:
    json.dump(veri,file,ensure_ascii=False,indent=4)

with open("ödev6.json","r",encoding = "utf-8") as file2:
    veriler = json.load(file2)
    sıralanmış_veriler = sorted(veriler,key=lambda x:x['Yaş'])

with open("ödev7.json","w",encoding = "utf-8") as file3:
    json.dump(sıralanmış_veriler,file3,ensure_ascii=False,indent=4)
