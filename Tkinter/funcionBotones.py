from tkinter import *
ventana = Tk()
ventana.title('Interfaz con Python')
ventana.resizable(0,0)
ventana.geometry('500x400')

def click_uno():
    lbl_uno.configure(text='Se presiono el boton 1')

def click_dos():
    lbl_uno.configure(text='Se presiono el boton 2')

btn1 = Button(ventana, text='Boton 1', command=click_uno)
btn1.grid(row=1,column=1)

btn2 = Button(ventana, text='boton 2', command=click_dos)
btn2.grid(row=1,column=2)

lbl_uno = Label(ventana, text='Presione un boton')
lbl_uno.grid(row=3,column=2)

ventana.mainloop()