from tkinter import *
# modulo de interfaz grafica para python

# crear ventana
ventana = Tk() 

ventana.title("Primer programa grafico")
ventana.resizable(0,0)  # evita que se pueda redimencionar la ventana
ventana.geometry("600x400") # ancho x altura

ventana['bg']='#49A'

# etiquetas
etiqueta1 = Label(ventana,text='etiqueta uno', font=('calibri', 20),bg='#49A', fg='azure')
etiqueta1.grid(row=0, column=2)

etiqueta2 = Label(ventana, text='etiqueta dos', font=('helvetica', 20), bg='#49A', fg='azure')
etiqueta2.place(x=100, y=100)

# botones
btn1 = Button(ventana, text='enviar', bg='azure', fg='#49A')
btn1.grid(row=1, column=1)

#generar el loop del programa para que no se termine hasta que se cierre
ventana.mainloop()