class Hayvan:
    def ses_cikar(self):
        pass

class Kus(Hayvan):
    def ses_cikar(self):
        print("CikCik")

class Kopek(Hayvan):
    def ses_cikar(self):
        print("HavHav")

class Kedi(Hayvan):
    def ses_cikar(self):
        print("MiyavMiyav")

def Hayvan_Sesleri(hayvan):
    hayvan.ses_cikar()

kus = Kus()

kopek = Kopek()

kedi = Kedi()

Hayvan_Sesleri(kus)
Hayvan_Sesleri(kedi)
Hayvan_Sesleri(kopek)