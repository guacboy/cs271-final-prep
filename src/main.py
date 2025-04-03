from tkinter import *

from util import *

root = Tk()
root.geometry("600x700")
root.config(background=BG_COLOR)

def main_menu() -> None:
    create_button = Util.button(root)
    create_button.config(text="Create Exam",
                         command=lambda: create_exam())
    create_button.pack(side=BOTTOM,
                       pady=(0, 50))

def create_exam() -> None:
    exam_window = Toplevel()  
    exam_window.geometry("800x600")
    exam_window.config(background=BG_COLOR)

if __name__ == "__main__":
    main_menu()
    root.mainloop()