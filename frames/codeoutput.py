from tkinter import *
import tkinter as tk
from tkinter import messagebox

from functions.configfuncs import get_message
from functions.screenshot import CaptureShell

from frames.reader_wait import OCRWait


class CaptureOutput(tk.Frame):
    def __init__(self, root, cursor):
        tk.Frame.__init__(self, root)
        self.root = root
        self.cursor = cursor
        main_frame = Frame(self.root, bg="cyan", relief=GROOVE)
        main_frame.place(x=10, y=10, width=480, height=480)

        intro_text = get_message('OutputSelect')
        introbox = Text(main_frame, bg="white", font=("times new roman", 11), padx=10, pady=10, width=50, height=5,
                        wrap=WORD)
        introbox.insert(INSERT, intro_text)
        introbox.place(y=60)

        self.counter = 1
        Button(main_frame, text='Capture', command=self.shell_capture, activebackground='cyan').place(x=220, y=250)
        Button(main_frame, text='NEXT', command=self.finish, activebackground='cyan').place(x=220, y=400)

    def shell_capture(self):
        x = CaptureShell(name=self.counter)
        msg = x.capture()
        if msg == 'fail':
            messagebox.showerror("Error!", "SHELL is not open!", parent=self.root)
        else:
            self.counter += 1

    def finish(self):
        OCRWait(self.root, self.cursor)