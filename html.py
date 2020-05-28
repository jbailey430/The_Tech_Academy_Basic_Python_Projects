import tkinter
from tkinter import *

class Window(Frame):
    def __init__(self, master):
        Frame. __init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

    
f = open("htmlPython.html", "a")
f.write("Stay tuned for our amazing summer sale!")
f.close()

f = open("htmlPython.html", "r")
print(f.read())
