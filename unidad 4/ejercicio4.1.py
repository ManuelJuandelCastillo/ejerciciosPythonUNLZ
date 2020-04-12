from tkinter import *
import random

def num10():
    lbl1.configure(text=random.randint(0,10))

def num50():
    lbl2.configure(text=random.randint(0,50))

def num100():
    lbl3.configure(text=random.randint(0,100))

ventana = Tk()
ventana.title('Numeros Random')
ventana.resizable(0,0)
ventana.geometry('400x400')

bt1 = Button(ventana, text="numero entre 0 y 10", command=num10)
bt1.grid(row=0, column=0)

bt2 = Button(ventana, text="numero entre 0 y 50", command=num50)
bt2.grid(row=0, column=1)

bt3 = Button(ventana, text="numero entre 0 y 100", command=num100)
bt3.grid(row=0, column=2)

lbl1 = Label(ventana)
lbl1.grid(row=1,column=0)

lbl2 = Label(ventana)
lbl2.grid(row=1,column=1)

lbl3 = Label(ventana)
lbl3.grid(row=1,column=2)

ventana.mainloop()