import tkinter
from tkinter import * #коммит

class GUI:
    def __init__(self, window):
        self.window = window
        window.title("The Little Alien")
        window.geometry('800x600')
        window.configure(bg="#87CEEB")


        self.title_frame = Frame(window, bg="#87CEEB")
        self.title_frame.grid(row=0, column=0, columnspan=3, pady=20)

        self.title_label = Label(self.title_frame, text='The Little Alien', font=("Arial Black", 32), bg="#87CEEB", fg="white")
        self.title_label.pack()





