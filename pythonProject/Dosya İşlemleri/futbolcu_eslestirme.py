def takımı_eslestir(temp):
    liste = temp.split(",")
    ismi = liste[0]
    takım = liste[1]
    return "Futbolcunun Adı: " + ismi + " Oynadığı takım:" +takım + '\n'
with open("futbolcular.txt","r",encoding="utf-8") as file:
    eklenecek_liste = []
    for i in file:
        eklenecek_liste.append(takımı_eslestir(i))

with open("fb.txt","w",encoding="utf-8") as file:
    for i in eklenecek_liste:
        if "Fenerbahçe" in i :
            file.write(i)

with open("gs.txt", "w", encoding="utf-8") as file2:
    for i in eklenecek_liste:
        if "Galatasaray" in i :
            file2.write(i)

with open("bjk.txt", "w", encoding="utf-8") as file3:
    for i in eklenecek_liste:
        if "Beşiktaş" in i :
            file3.write(i)