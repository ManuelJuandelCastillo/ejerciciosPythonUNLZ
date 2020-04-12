from tkinter import *

ventana = Tk()
ventana.title('Formulario')
ventana.resizable(0,0)
ventana.geometry('300x300')

def click():
    mensaje = texto.get()
    etiqueta2.configure(text=mensaje)
    texto.delete(0,len(mensaje))

etiqueta1 = Label(ventana, text='Texto a ingresar')
etiqueta1.grid(row=0,column=0)

etiqueta2 = Label(ventana, text='Ingrese un texto')
etiqueta2.grid(row=1,column=0)

texto = Entry(ventana)
texto.grid(row=0,column=1)

boton = Button(ventana, text="Aceptar", command=click)
boton.grid(row=0,column=2)

ventana.mainloop()