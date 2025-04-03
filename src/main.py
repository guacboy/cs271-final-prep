from tkinter import *

from util import *

root = Tk()
root.geometry("600x700")
root.config(background=BG_COLOR)

def main_menu() -> None:
    """
    Displays main menu GUI.
    """
    
    # creates the exam
    create_button = Util.button(root)
    create_button.config(text="Create Exam",
                         command=lambda: create_exam())
    create_button.pack(side=BOTTOM,
                       pady=(0, 50))

def create_exam() -> None:
    """
    Displays exam GUI.
    """
    
    # creates a new window (for the exam)
    exam_window = Toplevel()  
    exam_window.geometry("800x600")
    exam_window.config(background=BG_COLOR)
    
    # goes to previous question
    prev_button = Util.button(exam_window)
    prev_button.config(text="<",
                       padx=10,
                       pady=5,
                       command=lambda: print("prev"))
    prev_button.pack(side=LEFT,
                     padx=(15, 0))
    
    # goes to next question
    next_button = Util.button(exam_window)
    next_button.config(text=">",
                       padx=10,
                       pady=5,
                       command=lambda: print("next"))
    next_button.pack(side=RIGHT,
                     padx=(0, 15))
    
    # displays current question
    current_question_label = Util.label(exam_window)
    current_question_label.config(text="current question")
    current_question_label.pack(side=TOP)

if __name__ == "__main__":
    main_menu()
    root.mainloop()