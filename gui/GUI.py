import tkinter, json
from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window
        window.title("The Little Alien")
        window.geometry('800x600')
        window.configure(bg="#87CEEB") # голубой цвет


        self.title_frame = Frame(window, bg="#87CEEB") # это типа заголовок главная штукенция
        self.title_frame.grid(row=0, column=0, columnspan=3 , pady=20)

        self.title_label = Label(self.title_frame, text='The Little Alien', font=("Arial Black", 32), bg="#87CEEB", fg="white")
        self.title_label.pack()

        #теперь кнопочки
        self.button_frame = Frame(window, bg="#87CEEB")
        self.button_frame.grid(row=1, column=1, pady=20)

        self.button_start = Button(self.button_frame, text="Начать играть", width=20, height=2, bg="#90EE90", command=self.start_game)
        self.button_start.pack(pady=10)

        self.button_score = Button(self.button_frame, text="Смотреть рекорды", width=20, height=2, bg="#F0E68C", command=self.show_score)
        self.button_score.pack(pady=10)

        self.button_exit = Button(self.button_frame, text="Выйти из игры", width=20, height=2, bg="#FA8072", command=self.exit_game)
        self.button_exit.pack(pady=10)

        self.label_author = Label(window, text="Made by Inferno", font=("Arial", 12), bg="#87CEEB")
        self.label_author.grid(row=2, column=0, columnspan=3, sticky=tkinter.S, pady=10)

        # а тут изображение (+ метод на выброс ошибки)



    def start_game(self): pass


    def show_score(self): pass

    def exit_game(self): pass

    def load_highscores(self, filename='records.json'): #загрузка рекордов
        with open(filename, 'r') as file:
            data = json.load(file)
            self.highscores = data['records']

    

root = Tk()
gui = GUI(root)
root.mainloop()
