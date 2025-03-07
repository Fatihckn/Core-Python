import tkinter as tk
from tkinter import messagebox





def kaydet():
    tk.messagebox.showinfo(
        message=agreement.get()
    )


root = tk.Tk()
root.geometry('300x300')
root.title('Checkbox example')

agreement = tk.StringVar()

checkbox = tk.Checkbutton(
    text="Kabul ediyorum",
    variable = agreement,
    onvalue='Okey',
    offvalue=''
)
checkbox.pack()

checkbox2 = tk.Checkbutton(
    text='C++ Biliyorum.',
    variable=agreement,
    onvalue='Biliyorum',
    offvalue='Bilmiyorum' #başlangıçta offvalue boş bırakmazsak tikli gelir
)
checkbox2.pack()



button = tk.Button(text="Onayla",command=kaydet)
button.pack()



root.mainloop()