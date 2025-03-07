import tkinter as tk
import json

root = tk.Tk()
root.title("Telefon Rehberi")
root.geometry("400x300")
root.resizable(False, False)

def kisiekle():
    with open('ornek.json', 'a', encoding='utf-8') as f:
        veri = {
            'Adı': entry1.get(),
            'Telefon No': entry2.get(),
            'Adresi': entry3.get()
        }
        json.dump(veri, f, ensure_ascii=False, indent=4)

def kisisil():
    def kisisil():
        with open('ornek.json', 'r', encoding='utf-8') as f:
            dosya = json.load(f)

        print("Dosya içeriği:", dosya)

        silinecek_veri = {
            'Adı': entry1.get(),
            'Telefon No': entry2.get(),
            'Adresi': entry3.get()
        }

        print("Silinecek veri:", silinecek_veri)

        if silinecek_veri in dosya.values():
            print("Silinecek veri dosya içinde bulundu.")
            dosya = [kisi for kisi in dosya if kisi != silinecek_veri]
            with open('ornek.json', 'w', encoding='utf-8') as f:
                json.dump(dosya, f, ensure_ascii=False, indent=4)
            print("Kişi silindi")
        else:
            print("İstediğiniz kişi bulunamadı")


def kisibul():
    pass

label1 = tk.Label(root, text='Kişi Adı:')
label1.grid(row=0, column=0, sticky='w')

entry1 = tk.Entry(root, width=55)
entry1.grid(row=0, column=1, sticky='w')

label2 = tk.Label(root, text='Telefon Numarası:')
label2.grid(row=1, column=0, sticky='w')

entry2 = tk.Entry(root, width=55)
entry2.grid(row=1, column=1, sticky='w')

label3 = tk.Label(root, text='Kişi Adresi:')
label3.grid(row=2, column=0, sticky='w')

entry3 = tk.Entry(root, width=55)
entry3.grid(row=2, column=1, sticky='w')

dügme1 = tk.Button(root, text='Kişi Ekle', command=kisiekle)
dügme1.grid(row=3, columnspan=2, sticky='ew')

dügme2 = tk.Button(root, text='Kişi Sil', command=kisisil)
dügme2.grid(row=4, columnspan=2, sticky='ew')

dügme3 = tk.Button(root, text='Kişi Bul', command=kisibul)
dügme3.grid(row=5, columnspan=2, sticky='ew')

entry4 = tk.Entry(root, width=55)
entry4.grid(row=6, columnspan=2, sticky='ew')

root.mainloop()
