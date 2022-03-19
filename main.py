import tkinter as tk
from windows.index import MainWindow
from functions.configfuncs import create_screenshot_dir


def main():
    root = tk.Tk()
    root.withdraw()
    create_screenshot_dir()
    MainWindow(master=root)
    root.mainloop()


if __name__ == '__main__':
    main()
