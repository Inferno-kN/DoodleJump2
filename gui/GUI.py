import tkinter
from tkinter import * #коммит

window = Tk() #коммит
window.title("The Little Alien") #коммит
window.geometry('800x600')
lbl = Label(window, text="Добро пожаловать!", font=("Arial Bold", 20))
lbl.grid(column=10, row=10)
lbl.place(x=270, y=30)

btn = tkinter.Button(text='Начать игру')
btn.place(x=340, y=200)

btn1 = tkinter.Button(text='Посмотреть статистику рекордов')
btn1.place(x=285, y=260)

btn2 = tkinter.Button(text='Выйти из игры')
btn2.place(x=335, y=320)



