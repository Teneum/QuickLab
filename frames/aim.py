from tkinter import *
import tkinter as tk
from frames.suggestions import Suggestions
from functions.configfuncs import get_message

class Aim(tk.Frame):
    def __init__(self, root, cursor):
        tk.Frame.__init__(self, root)
        self.root = root
        self.cursor = cursor
        main_frame = Frame(self.root, bg="cyan", relief=GROOVE)
        main_frame.place(x=10, y=10, width=480, height=480)

        intro_text = get_message(header='Aim')
        Label(main_frame, text=intro_text, font=("times new roman", 11), bg="white",
              fg="black", relief=RAISED).place(x=20, y=20)
        self.aimtextbox = Text(main_frame, height=10, width=45)
        self.aimtextbox.place(y=85, x= 20)
        Button(main_frame, text='NEXT', command=self.finish, activebackground='cyan').place(x=220, y=350)

    def finish(self):
        input = self.aimtextbox.get("1.0", 'end-1c')
        self.cursor.aim(input.capitalize())
        Suggestions(self.root, self.cursor, aim=input)
