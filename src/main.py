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
    create_button.bind("<Enter>", func=lambda e: on_option_hover(create_button))
    create_button.bind("<Leave>", func=lambda e: on_option_hover(create_button))
    create_button.pack(side=BOTTOM,
                       pady=(0, 50))

def create_exam() -> None:
    """
    Displays exam GUI.
    """
    
    # creates a new window (for the exam)
    exam_window = Toplevel()  
    exam_window.geometry("950x700")
    exam_window.config(background=BG_COLOR)
    
    # goes to previous question
    prev_button = Util.button(exam_window)
    prev_button.config(text="<",
                       padx=10,
                       pady=5,
                       command=lambda: print("prev"))
    prev_button.bind("<Enter>", func=lambda e: on_option_hover(prev_button))
    prev_button.bind("<Leave>", func=lambda e: on_option_hover(prev_button))
    prev_button.pack(side=LEFT,
                     padx=(15, 0))
    
    # goes to next question
    next_button = Util.button(exam_window)
    next_button.config(text=">",
                       padx=10,
                       pady=5,
                       command=lambda: print("next"))
    next_button.bind("<Enter>", func=lambda e: on_option_hover(next_button))
    next_button.bind("<Leave>", func=lambda e: on_option_hover(next_button))
    next_button.pack(side=RIGHT,
                     padx=(0, 15))
    
    # displays current question
    current_question_label = Util.label(exam_window)
    current_question_label.config(text="current question")
    current_question_label.pack(side=TOP)
    
    # question navigator frame
    question_navigator_frame = Util.frame(exam_window)
    
    question_navigator = {}
    # creates "i" amount of question navigator buttons
    for i in range(1, 31):
        # allows to navigate to different questions
        question_navigator_button = Util.button(question_navigator_frame)
        question_navigator_button.config(text="○",
                                         font=(FONT, 15, "normal"),
                                         bg=BG_COLOR,
                                         activebackground=BG_COLOR,
                                         padx=0,
                                         pady=0,
                                         relief=FLAT,
                                         bd=0,
                                         command=lambda button=i: print(button),)
        # binds each button to a hover effect
        question_navigator_button.bind("<Enter>", lambda e, button=question_navigator_button: on_question_navigator_hover(button))
        question_navigator_button.bind("<Leave>", lambda e, button=question_navigator_button: on_question_navigator_hover(button))
        question_navigator_button.pack(side=LEFT)
        
        # creates a button hashmap for easier access
        question_navigator["Q" + str(i)] = question_navigator_button
        
    def on_question_navigator_hover(button) -> None:
        """
        Changes the button texture in accordance
        to mouse position vs button
        """
        
        button.bind("<Enter>", func=lambda e: button.config(text="◉"))
        button.bind("<Leave>", func=lambda e: button.config(text="○"))
        
    question_navigator_frame.pack(side=BOTTOM,
                                  pady=(0, 20),)

def on_option_hover(button) -> None:
    button.bind("<Enter>", func=lambda e: button.config(bg=HOVER_COLOR))
    button.bind("<Leave>", func=lambda e: button.config(bg=OPTION_COLOR))

if __name__ == "__main__":
    main_menu()
    root.mainloop()