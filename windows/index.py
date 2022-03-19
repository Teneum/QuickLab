import tkinter as tk
from tkinter import ttk, Label, Frame, Entry, Button, messagebox

from frames.maindetail import MainDetail
from functions.configfuncs import clear_image_paths, clear_file_path
import sys

from writer import Writer
cursor = Writer(None, None, None, None)


class MainWindow:
    def __init__(self, master):
        super().__init__()
        self.root = tk.Toplevel(master)
        self.root.title("LabExercise Automation - Shashank Shukla")  # For Title of the page
        self.root.geometry("500x500")  # Resolution of the page , top, bottom
        self.root.config(bg="white")

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                clear_image_paths()
                clear_file_path()
                self.root.destroy()
                sys.exit()
        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        MainDetail(self.root)
