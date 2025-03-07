import tkinter as tk

root = tk.Tk()

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=5)
root.columnconfigure(2,weight=1)


label1 = tk.Label(root, text="0-0")
label1.grid(row=0, column=0)         #row kaçıncı satırdaa olduğu, column ise hangi sütunda olacağı

label2 = tk.Label(root, text="1-0")
label2.grid(row=1, column=0)

button = tk.Button(root, text="1-1")
button.grid(row=1, column=1)


label3 = tk.Label(root, text="3-2")
label3.grid(row=3, column=2)

root.mainloop()