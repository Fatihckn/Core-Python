import tkinter as tk
pencere = tk.Tk()
def olustur():
    dosya = open("deneme.txt", "w")
dugme = tk.Button(text = "oluştur", command=olustur)
dugme.pack()

dugme2 = tk.Button(text = "çıkıs", command=pencere.quit)
dugme2.pack()

tk.mainloop()
