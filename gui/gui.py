import sys
import tkinter, json
from tkinter import *
from refactoring.source.MainLoop import MainLoop
from refactoring.source.StorageManager import StorageManager

class GUI:
    def __init__(self, window):
        self.window = window
        self.__directory = StorageManager()
        #self.__background = Background()
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


    def start_game(self):
        self.window.withdraw()  # Скрываем главное окно
        mainloop = MainLoop()
        self.game_window = Toplevel(self.window)  # создаем новое окно для игры
        self.game_window.title("Игра началась!")
        self.game_window.geometry('800x600')
        self.game_window.configure(bg="#87CEEB")
        mainloop.run()



        label = Label(self.game_window, font=("Arial", 24), bg="#87CEEB", fg="white")
        label.pack(pady=20)

        button_end_game = Button(self.game_window, text="Выйти в главное меню", command=self.end_game)
        button_end_game.pack(pady=10)
        button_end_game.place(relx=1.0, rely=0.0, anchor=NE)

    def end_game(self):
        self.game_window.destroy()  # закрываем окно игры
        self.window.deiconify()  # показываем главное окно снова

    def show_score(self):
        score_window = Toplevel(self.window)
        score_window.title("Records")
        score_window.geometry("300x200")

        path_records = self.__directory.get_records()

        try:
            with open(path_records, "r") as file:
                scores = json.load(file)
            display_text = ', '.join(str(elem) for elem in scores)
        except (FileNotFoundError, json.JSONDecodeError):
            display_text = "Нет данных или ошибка файла"

        label_author = Label(score_window, text=display_text, font=("Arial", 12))
        label_author.pack(pady=10)

        close_button = Button(score_window, text="Закрыть", command=score_window.destroy)
        close_button.pack(pady=10)

    def exit_game(self):
        self.window.destroy()
        sys.exit()

root = Tk()
gui = GUI(root)
root.mainloop()



