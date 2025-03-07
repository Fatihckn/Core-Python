import tkinter as tk
class Uygulama:
    def __init__(self):
       self.araclar()
    def araclar(self):
       self.etiket = tk.Label(text="Dosyayı silmek istedi˘ginizden emin misiniz?")
       self.etiket.pack()
pencere = tk.Tk()
uyg = Uygulama()
tk.mainloop()
