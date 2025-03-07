import tkinter as tk
from tkinter import messagebox

# Oyun tahtası (3x3'lük bir liste)
tahta = [' ' for _ in range(9)]
oyuncu = 'X'

# Kazanma kombinasyonları
kazanan_kombinasyonlar = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Satırlar
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Sütunlar
    [0, 4, 8], [2, 4, 6]  # Çaprazlar
]


# Kazanma durumunu kontrol eden fonksiyon
def kazanan_var_mi(oyuncu):
    for kombinasyon in kazanan_kombinasyonlar:
        if all(tahta[i] == oyuncu for i in kombinasyon):
            return True
    return False


# Beraberlik durumunu kontrol eden fonksiyon
def beraberlik_var_mi():
    return all(yer != ' ' for yer in tahta)


# Hamle yapıldığında çalışacak fonksiyon
def hamle_yap(button, pozisyon):
    global oyuncu
    if tahta[pozisyon] == ' ':
        tahta[pozisyon] = oyuncu
        button.config(text=oyuncu)

        # Kazanma veya beraberlik kontrolü
        if kazanan_var_mi(oyuncu):
            messagebox.showinfo("Oyun Bitti", f"Tebrikler! Oyuncu {oyuncu} kazandı!")
            pencere.destroy()
        elif beraberlik_var_mi():
            messagebox.showinfo("Oyun Bitti", "Oyun berabere!")
            pencere.destroy()
        else:
            # Oyuncuyu değiştir
            oyuncu = 'O' if oyuncu == 'X' else 'X'
    else:
        messagebox.showwarning("Geçersiz Hamle", "Bu pozisyon dolu! Başka bir pozisyon seçin.")


# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Tik Tak Toe")

# Butonları oluştur ve pencereye yerleştir
butonlar = []
for i in range(9):
    button = tk.Button(pencere, text=" ", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: hamle_yap(butonlar[i], i))
    button.grid(row=i // 3, column=i % 3)
    butonlar.append(button)

# Oyunu başlat
pencere.mainloop()
