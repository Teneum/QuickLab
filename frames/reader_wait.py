from tkinter import *
import tkinter as tk
from tkinter import messagebox

from functions.configfuncs import get_message

import sys


class OCRWait(tk.Frame):
    def __init__(self, root, cursor):
        tk.Frame.__init__(self, root)
        self.root = root
        self.cursor = cursor
        main_frame = Frame(self.root, bg="cyan", relief=GROOVE)
        main_frame.place(x=10, y=10, width=480, height=480)

        intro_text = get_message('OCRWait')
        introbox = Text(main_frame, bg="white", font=("times new roman", 11), padx=10, pady=10, width=50, height=5,
                        wrap=WORD)
        introbox.insert(INSERT, intro_text)
        introbox.place(y=60)
        self.cursor.sample_output()
        self.cursor.screenshots()
        Button(main_frame, text='FINISH', command=self.finish, activebackground='cyan').place(x=220, y=400)

    def finish(self):

        self.cursor.finish_doc()
        self.root.destroy()
        sys.exit()

