import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from writer import Writer
from frames.aim import Aim

from functions.configfuncs import *



class MainDetail(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        main_frame = Frame(self.root, bg="cyan", relief=GROOVE)
        main_frame.place(x=10, y=10, width=480, height=480)

        Label(main_frame, text="CS LabEx Automator", font=("times new roman", 20, "bold"), bg="white",
              fg="black", relief=RAISED).place(x=120, y=20)

        intro_text = get_message(header="Intro")
        introbox = Text(main_frame, bg="white", font=("times new roman", 11), padx=10, pady=10, width=50, height=4,
                        wrap=WORD)
        introbox.insert(INSERT, intro_text)
        introbox.place(y=60)

        details = get_user_details()

        Label(main_frame, text="Name:", font=("times new roman", 14, "bold")).place(x=10, y=200)
        self.txtname = Entry(main_frame, font=("times new roman", 14))
        self.txtname.place(x=125, y=200, width=300)
        self.txtname.insert(0, details['Name'])

        Label(main_frame, text="Section:", font=("times new roman", 14, "bold")).place(x=10, y=235)
        self.section = Entry(main_frame, font=("times new roman", 14))
        self.section.place(x=125, y=235, width=300)
        self.section.insert(0, details['Section'])

        Label(main_frame, text="Date:", font=("times new roman", 14, "bold")).place(x=10, y=270)
        self.txtdate = Entry(main_frame, font=("times new roman", 14))
        self.txtdate.place(x=125, y=270, width=300)

        Label(main_frame, text="Exercise No:", font=("times new roman", 14, "bold")).place(x=10, y=305)
        self.exno = Entry(main_frame, font=("times new roman", 14))
        self.exno.place(x=175, y=305, width=300)

        Button(main_frame, text='NEXT', command=self.finish, activebackground='cyan').place(x=220, y=340)

    def finish(self):
        name = self.txtname.get()
        section = self.section.get()
        date = self.txtdate.get()
        exno = self.exno.get()
        condition = (len(name) and len(section) and len(date) and len(exno))
        if condition == 0:
            messagebox.showerror("Error!", "All Fields are Required!", parent=self.root)
        else:
            cursor = Writer(stud_name=name, date=date, section=section, ex_no=exno)
            set_user_details(name=name, section=section)
            Aim(self.root, cursor)