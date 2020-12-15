"""lesson1.py - message box: creates a tk message box"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

messagebox.showinfo('Bobby\' World', 'Hello Y\'all! This is a message from Bobby\nThis is some really cool stuff')