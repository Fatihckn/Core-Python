import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('400x400+100+100')

def diyalogu_goster():
    result = tk.messagebox.askyesno("Bilgi Kutusu","Onaylıyor musunuz")
    if result == True:
        print("Onaylandı.")
    else:
        print("Onaylanmadı")




buton = tk.Button(root,text="DiyalogKutusunu Göster",command=diyalogu_goster)
buton.pack()


root.mainloop()