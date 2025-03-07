import tkinter as tk

root = tk.Tk()
root.geometry('500x500')
root.resizable(False,False)
root.title('Hesap Makinesi')

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)


entry = tk.Entry(root, font=('Helvetica', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
entry.bind("<Key>", "break")

def sayıgir(a):
    entry.insert(tk.END,a)

def tamamı_sil():
    entry.delete(0,tk.END)

def hesapla():
    entry_icerik = entry.get()
    #if entry_icerik[-1] == '+' or entry_icerik[-1] == '-' or entry_icerik[-1] == '/' or entry_icerik[-1] == '*':

    try:
        temp = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(temp))
    except SyntaxError:
        entry.delete(0, tk.END)
        temp = "Hatalı İşlem! Devam Etmek için 'C' ile sıfırlayınız."
        entry.insert(tk.END,temp)
def sil():
    entry.delete(len(entry.get())-1, tk.END)



dugme1 = tk.Button(root,text='7',command=lambda :sayıgir('7'),height=3,width=5,)
dugme1.grid(row = 1,column = 0)

dugme2 = tk.Button(root,text='8',command=lambda :sayıgir('8'),height=3,width=5)
dugme2.grid(row = 1,column = 1)

dugme3 = tk.Button(root,text='9',command=lambda :sayıgir('9'),height=3,width=5)
dugme3.grid(row = 1,column = 2)

dugme4 = tk.Button(root,text='/',command=lambda :sayıgir('/'),height=3,width=5,bg="yellow")
dugme4.grid(row = 1,column = 3)

dugme5 = tk.Button(root,text='4',command=lambda :sayıgir('4'),height=3,width=5)
dugme5.grid(row = 2,column = 0)

dugme6 = tk.Button(root,text='5',command=lambda :sayıgir('5'),height=3,width=5)
dugme6.grid(row = 2,column = 1)

dugme7 = tk.Button(root,text='6',command=lambda :sayıgir('6'),height=3,width=5)
dugme7.grid(row = 2,column = 2)

dugme8 = tk.Button(root,text='*',command=lambda :sayıgir('*'),height=3,width=5,bg="yellow")
dugme8.grid(row = 2,column = 3)

dugme9 = tk.Button(root,text='1',command=lambda :sayıgir('1'),height=3,width=5)
dugme9.grid(row = 3,column = 0)

dugme10 = tk.Button(root,text='2',command=lambda :sayıgir('2'),height=3,width=5)
dugme10.grid(row = 3,column = 1)

dugme11 = tk.Button(root,text='3',command=lambda :sayıgir('3'),height=3,width=5)
dugme11.grid(row = 3,column = 2)

dugme12= tk.Button(root,text='-',command=lambda :sayıgir('-'),height=3,width=5,bg="yellow")
dugme12.grid(row = 3,column = 3)

dugme13 = tk.Button(root,text='C',command=lambda :tamamı_sil(),height=3,width=5,bg="red")
dugme13.grid(row = 4,column = 0)

dugme14 = tk.Button(root,text='0',command=lambda :sayıgir('0'),height=3,width=5)
dugme14.grid(row = 4,column = 1)

dugme15 = tk.Button(root,text='=',command=lambda :hesapla(),height=3,width=5,bg="yellow")
dugme15.grid(row = 4,column = 2)

dugme16= tk.Button(root,text='+',command=lambda :sayıgir('+'),height=3,width=5,bg="yellow")
dugme16.grid(row = 4,column = 3)

dugme17= tk.Button(root,text='<-',command=lambda :sil(),height=3,width=5,bg="yellow")
dugme17.grid(row = 5,column = 0)




root.mainloop()