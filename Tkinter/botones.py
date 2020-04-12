from tkinter import *
ventana = Tk()
ventana.title('Interfaz con Python')
ventana.resizable(0,0)
ventana.geometry('500x400')

btn1 = Button(ventana, text='simple')
btn1.grid(row=1, column=0)

btn2 = Button(ventana, text='flat', relief=FLAT)
btn2.grid(row=1, column=1)

btn3 = Button(ventana, text='sunken', relief=SUNKEN)
btn3.grid(row=1, column=2)

btn4 = Button(ventana, text='ridge', relief=RIDGE)
btn4.grid(row=1, column=3)

btn5 = Button(ventana, text='solid', relief=SOLID)
btn5.grid(row=1, column=4)

ventana.mainloop()