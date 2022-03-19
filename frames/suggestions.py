from tkinter import *
import tkinter as tk


from frames.algo import Algo
from functions.configfuncs import get_message
from functions.search import search
from functions.hyperlink import Hyperlink


class Suggestions(tk.Frame):
    def __init__(self, root, cursor, aim):
        tk.Frame.__init__(self, root)
        self.root = root
        self.cursor = cursor
        main_frame = Frame(self.root, bg="cyan", relief=GROOVE)
        main_frame.place(x=10, y=10, width=480, height=480)

        intro_text = get_message(header='Search')
        Label(main_frame, text=intro_text, font=("times new roman", 15), bg="white",
              fg="black", relief=RAISED).place(x=20, y=20)

        results = search(aim+' in python')
        y = 65
        for i, result in enumerate(results, start=1):
            hlink = Hyperlink(main_frame, text=f"{i}. " + result['Title'], link=result['Link'])
            hlink.place(x=20, y=y)
            y += 35

        Button(main_frame, text='NEXT', command=self.finish, activebackground='cyan').place(x=220, y=440)

    def finish(self):
        Algo(self.root, self.cursor)
