import tkinter as tk
import random
pencere = tk.Tk()
pencere.geometry("300x50+600+460")
def kodlar():
   liste = []
   for i in range(6):
      while len(liste) != 6:
         a = random.randint(1,100)
         if a not in liste:
            liste.append(a)
   etiket["text"] = liste
etiket = tk.Label(text="Sayı üretmek için dü˘gmeye basınız!",
fg="white",
bg="#61380B",
font="Helvetica 12 bold")
etiket.pack()
dugme = tk.Button(text="Yeniden",command=kodlar)
dugme.pack()
tk.mainloop()