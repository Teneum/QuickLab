from tkinter import filedialog as fd
from functions.configfuncs import set_selected_file


def select_file():
    filetypes = (
        ('Python Files', '*.py'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    set_selected_file(path=filename)


def open_file(path):
    try:
        with open(path, "r") as f:
            s = f.read()
            return s
    except Exception as e:
        print(e)
