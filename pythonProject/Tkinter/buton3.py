import tkinter as tk
from tkinter import messagebox



# verdiğimiz resmi, PhotoImage dosyasına çevirmem gerekmektedir.
# bu imageyi image parametresi olarak buttona verebiliriz.

def download_clicked():
    tk.messagebox.showinfo(
        title='Bilgi',
        message='İndirme Butonuna Tıklandı, İndirme başarıyla başlatıldı.'
    )

root = tk.Tk()
root.geometry('300x300+50+50')
root.title('İmage button demo')

download_icon=tk.PhotoImage(file='indir.png')
download_button= tk.Button(root,image=download_icon,text="Download",command=download_clicked, compound=tk.LEFT)

download_button.pack(
    ipadx=15,
    ipady=15
)


root.mainloop()