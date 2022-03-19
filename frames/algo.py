from tkinter import *
import tkinter as tk
from frames.pyfile_select import PyFileSelect


class Algo(tk.Frame):
    def __init__(self, root, cursor):
        tk.Frame.__init__(self, root)
        self.root = root
        self.cursor = cursor
        main_frame = Frame(self.root, bg="cyan", relief=GROOVE)
        main_frame.place(x=10, y=10, width=480, height=480)

        intro_text = "Enter Algorithm/Method for The Exercise. Click on NEXT when done"
        Label(main_frame, text=intro_text, font=("times new roman", 10), bg="white",
              fg="black", relief=RAISED).place(x=2, y=20)

        self.algotextbox = Text(main_frame, height=17, width=50, font=("times new roman", 11))
        self.algotextbox.place(y=85, x=20)
        Button(main_frame, text='NEXT', command=self.finish, activebackground='cyan').place(x=220, y=420)

    def finish(self):
        input = self.algotextbox.get("1.0", 'end-1c')
        self.cursor.algorithm(input)
        PyFileSelect(self.root, self.cursor)