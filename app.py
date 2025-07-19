import tkinter
from src.Gui import GUI

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    gui.start_game()
    root.mainloop()