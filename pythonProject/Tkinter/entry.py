import tkinter as tk
pencere = tk.Tk()
def sil():
    giris.delete(len(giris.get()) - 1, tk.END)
    """yeniGiris = giris.get()
    giris.delete(0,tk.END)
    giris.insert(0,yeniGiris[0:len(yeniGiris)-1])"""
giris = tk.Entry() #giris.get dediğimizde entry'e yazdığımız şeye erişebiliyoruz(kapsülleme)
giris.pack()

dugme1 = tk.Button(text = "KAPAT", command = pencere.quit)
dugme1.pack()
dugme2 = tk.Button(text = "SIL", command = sil)
dugme2.pack()
tk.mainloop()