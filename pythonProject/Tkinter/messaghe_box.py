import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('400x400+100+100')

def diyalogu_goster():
    result = True
    while result == True:
        result = tk.messagebox.askretrycancel("Bilgi Butonu","Tekrar denemek istermisiniz")
        if result == True:
            print("Tekrar denendi.")
        else:
            print("Hata alındı.")




buton = tk.Button(root,text="DiyalogKutusunu Göster",command=diyalogu_goster)
buton.pack()


root.mainloop()