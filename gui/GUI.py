import tkinter
from tkinter import * #коммит

window = Tk() #коммит
window.title("The Little Alien") #коммит
window.geometry('800x600')
lbl = Label(window, text="Добро пожаловать!", font=("Arial Bold", 20))
lbl.grid(column=10, row=10)
lbl.place(x=270, y=30)


