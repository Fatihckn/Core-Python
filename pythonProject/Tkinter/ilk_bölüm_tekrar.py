import tkinter as tk
import random
liste = []
pencere = tk.Tk()
pencere.geometry("200x50+600+460")
etiket = tk.Label(fg="white", bg="#61380B",font="Helvetica 12 bold")
etiket.pack()
for i in range(6):
   while len(liste) != 6:
      a = random.randint(1,100)
      if a not in liste:
         liste.append(a)
etiket["text"] = liste
tk.mainloop()

