import tkinter as tk
pencere = tk.Tk()
pencere.geometry("100x500+15+100") #15 sağ-sol hareket eder, +100 dediğimiz yukarı aşşağı gider
etiket = tk.Label(text="Hata!")
pencere.resizable(width=False, height=False) #height yukarı aşşağı, width yatay olarak pencerenin oynatılmasını engeller
etiket.pack()
tk.mainloop()
