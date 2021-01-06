from tkinter import *

class Window:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("500x400")
        self.master.title("My App")
        self.frame.pack()


def main():
    root = Tk()
    app = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()