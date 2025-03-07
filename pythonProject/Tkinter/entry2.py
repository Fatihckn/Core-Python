import tkinter as tk
pencere = tk.Tk()
def olustur():
   dosya = open("deneme.txt","w")
   metin = giris.get()
   dosya.write(metin)
giris = tk.Entry()
giris.pack()
dugme = tk.Button(text = "OLU¸STUR", command = olustur)
dugme.pack()
dugme2 = tk.Button(text = "ÇIK", command = pencere.quit)
dugme2.pack()
tk.mainloop()
