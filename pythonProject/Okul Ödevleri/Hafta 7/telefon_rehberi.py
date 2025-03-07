import tkinter as tk
import json
import os

root = tk.Tk()
root.title("Telefon Rehberi")
root.geometry("400x300")
root.resizable(False,False)

if os.path.exists('ornek.json'):
    pass
else:
    with open('ornek.json', 'a', encoding='utf-8') as f:
        veri = {
            "Adı": [],
            "Telefon No": [],
            "Adresi": []
        }
        json.dump(veri, f, ensure_ascii=False)


def kisiekle():

    with open('ornek.json', 'r', encoding='utf-8') as f:
        dosya = json.load(f)
    dosya["Adı"].append(entry1.get())
    dosya["Telefon No"].append(entry2.get())
    dosya["Adresi"].append(entry3.get())
    with open('ornek.json', 'w', encoding='utf-8') as f:
        json.dump(dosya, f, ensure_ascii=False)
    bildiri = "Kişi Eklendi"
    entry4.delete(0,tk.END)
    entry4.insert(tk.END,bildiri)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
def kisisil():
    with open('ornek.json', 'r', encoding='utf-8') as f:
        dosya = json.load(f)


    silinecek_veri = {
            "Adı": entry1.get(),
            "Telefon No": entry2.get(),
            "Adresi": entry3.get()
        }

    if silinecek_veri["Telefon No"] in dosya["Telefon No"]:
        for anahtar, degerler in dosya.items():
            flag = 0
            for deger in degerler:
                if anahtar == "Adı":
                    if deger == silinecek_veri["Adı"] and flag == 0:
                        dosya[anahtar].remove(deger)
                        flag = 1

                elif anahtar == "Telefon No":
                    if deger == silinecek_veri["Telefon No"] and flag == 0:
                        dosya[anahtar].remove(deger)
                        flag = 1
                elif anahtar == "Adresi":
                    if deger == silinecek_veri["Adresi"] and flag == 0:
                        dosya[anahtar].remove(deger)
                        flag = 1
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
    else:
        entry4.delete(0,tk.END)
        temp = "Kişi Bulunamadı"
        entry4.insert(tk.END,temp)
    with open('ornek.json', 'w', encoding='utf-8') as f:
        json.dump(dosya, f, ensure_ascii=False)

def kisibul():
    with open('ornek.json', 'r', encoding='utf-8') as f:
        dosya = json.load(f)

    silinecek_veri = {
        "Adı": entry1.get(),
        "Telefon No": entry2.get(),
        "Adresi": entry3.get()
    }

    entry4.delete(0, tk.END)

    if silinecek_veri["Telefon No"] in dosya["Telefon No"]:
        for anahtar, degerler in dosya.items():
            flag = 0
            for deger in degerler:
                if anahtar == "Adı":
                    if deger == silinecek_veri["Adı"] and flag == 0:
                        temp = "Adı:" + deger + " "
                        entry4.insert(tk.END, temp)
                        flag = 1

                elif anahtar == "Telefon No":
                    if deger == silinecek_veri["Telefon No"] and flag == 0:
                        temp = "Telefon Numarası" + deger + " "
                        entry4.insert(tk.END, temp)
                        flag = 1
                elif anahtar == "Adresi":
                    if deger == silinecek_veri["Adresi"] and flag == 0:
                        temp = "Adresi:" + deger + " "
                        entry4.insert(tk.END, temp)
                        flag = 1
    else:
        entry4.delete(0,tk.END)
        temp = "Kişi Bulunamadı"
        entry4.insert(tk.END,temp)


label1 = tk.Label(root,text='Kişi Adı:')
label1.grid(row= 0,column= 0,sticky= 'w')

entry1 = tk.Entry(root,width= 55)
entry1.grid(row= 0,column= 1,sticky= 'w')

label2 = tk.Label(root,text='Telefon Numarası:')
label2.grid(row= 1,column= 0,sticky= 'w')

entry2 = tk.Entry(root,width= 55)
entry2.grid(row= 1,column= 1,sticky= 'w')

label3 = tk.Label(root,text='Kişi Adresi:')
label3.grid(row= 2,column= 0,sticky= 'w')

entry3 = tk.Entry(root,width= 55)
entry3.grid(row= 2,column= 1,sticky= 'w')

dügme1 = tk.Button(root,text='Kişi Ekle',command=lambda :kisiekle())
dügme1.grid(row= 3,columnspan=2,sticky='ew')

dügme2 = tk.Button(root,text='Kişi Sil',command=lambda :kisisil())
dügme2.grid(row= 4,columnspan=2,sticky='ew')

dügme3 = tk.Button(root,text='Kişi Bul',command=lambda :kisibul())
dügme3.grid(row= 5,columnspan=2,sticky='ew')

entry4 = tk.Entry(root,width= 55)
entry4.grid(row= 6,columnspan=2,sticky= 'ew')

root.mainloop()