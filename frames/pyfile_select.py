from tkinter import *
import tkinter as tk

from frames.codeoutput import CaptureOutput

from functions.configfuncs import get_message
from functions.read_py_file import select_file
from functions.configfuncs import get_selected_file

class PyFileSelect(tk.Frame):
    def __init__(self, root, cursor):
        tk.Frame.__init__(self, root)
        self.root = root
        self.cursor = cursor
        self.path = ''
        main_frame = Frame(self.root, bg="cyan", relief=GROOVE)
        main_frame.place(x=10, y=10, width=480, height=480)

        intro_text = get_message(header='FileSelect')
        Label(main_frame, text=intro_text, font=("times new roman", 15), bg="white",
              fg="black", relief=RAISED).place(x=20, y=20)

        selectbtn = Button(main_frame, text='Select File', command=self.file_select, width=10, height=2)
        selectbtn.place(x=200, y=100)
        Label(main_frame, text='Selected File is: ', font=("times new roman", 15), bg="white",
              fg="black", relief=RAISED).place(x=20, y=200)
        self.pathbox = Text(main_frame, bg="white", font=("times new roman", 8), padx=10, pady=10, width=30, height=3
                        )
        self.pathbox.place(x=180, y=200)
        Button(main_frame, text='NEXT', command=self.finish, activebackground='cyan').place(x=220, y=350)


    def file_select(self):
        select_file()
        self.path = get_selected_file()
        self.pathbox.insert(INSERT, self.path)

    def finish(self):
        self.cursor.source_code()
        CaptureOutput(self.root, self.cursor)
