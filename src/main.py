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
    
    global current_question_idx
    
    current_question_idx = 1
    
    # creates a new window (for the exam)
    exam_window = Toplevel()  
    exam_window.geometry("950x700")
    exam_window.config(background=BG_COLOR)
    
    # question information frame
    question_information_frame = Util.frame(exam_window)
    question_information_frame.config(bg=INFORMATION_BG_COLOR,
                                      pady=10,)
    
    # displays the current question number
    question_number_label = Util.label(question_information_frame)
    question_number_label.config(text=f"Question {current_question_idx}",
                                 bg=INFORMATION_BG_COLOR,)
    question_number_label.pack(side=LEFT,
                               padx=(15, 0))
    
    # ends the exam
    end_exam_button = Util.button(question_information_frame)
    end_exam_button.config(text="END",
                           padx=5,
                           pady=0,)
    end_exam_button.pack(side=RIGHT,
                         padx=(0, 15))
    
    # displays the timer
    timer_label = Util.label(question_information_frame)
    timer_label.config(text="00:00",
                       bg=INFORMATION_BG_COLOR)
    timer_label.pack(side=RIGHT,
                     padx=(0, 370))
    
    question_information_frame.pack(side=TOP,
                                    fill=BOTH,)
    
    # goes to previous question
    prev_button = Util.button(exam_window)
    prev_button.config(text="<",
                       padx=10,
                       pady=5,
                       command=lambda: display_current_question("prev",
                                                                question_number_label))
    prev_button.bind("<Enter>", func=lambda e: on_option_hover(prev_button))
    prev_button.bind("<Leave>", func=lambda e: on_option_hover(prev_button))
    prev_button.pack(side=LEFT,
                     padx=(15, 0))
    
    # goes to next question
    next_button = Util.button(exam_window)
    next_button.config(text=">",
                       padx=10,
                       pady=5,
                       command=lambda: display_current_question("next",
                                                                question_number_label))
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
        # TODO: add indicator which question you are on
        
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
                                         command=lambda i=i: display_current_question(str(i),
                                                                                      question_number_label))
        # binds each button to a hover effect
        question_navigator_button.bind("<Enter>", lambda e, button=question_navigator_button: on_question_navigator_hover(button))
        question_navigator_button.bind("<Leave>", lambda e, button=question_navigator_button: on_question_navigator_hover(button))
        question_navigator_button.pack(side=LEFT)
        
        # creates a button hashmap for easier access
        question_navigator["Q" + str(i)] = question_navigator_button
        
    def on_question_navigator_hover(button) -> None:
        """
        Changes the button texture in accordance
        to mouse position vs button.
        """
        
        button.bind("<Enter>", func=lambda e: button.config(text="◉"))
        button.bind("<Leave>", func=lambda e: button.config(text="○"))
        
    question_navigator_frame.pack(side=BOTTOM,
                                  pady=(0, 20),)

def display_current_question(action: str, question_number_label: Label) -> None:
    """
    Displays the current question
    and updates any relevant information.
    """
    
    global current_question_idx    
    
    # if action is "next", navigates to the next question
    if action == "next":
        current_question_idx += 1
    # if action is "prev", navigates to the previous question
    elif action == "prev":
        current_question_idx -= 1
    # otherwise, updates current_question_idx
    # to action parameter (new question idx)
    else:
        current_question_idx = int(action)
    
    # if attempting to navigate past the maximum questions
    if current_question_idx > 30:
        # loop back to the first question
        current_question_idx = 1
    # if attempting to navigate below the minimum questions
    elif current_question_idx < 1:
        # loop back to the last question
        current_question_idx = 30
        
    # updates display information
    question_number_label.config(text=f"Question {current_question_idx}")

def on_option_hover(button) -> None:
    """
    Changes the button texture in accordance
    to mouse position vs button.
    """   
    
    button.bind("<Enter>", func=lambda e: button.config(bg=HOVER_COLOR))
    button.bind("<Leave>", func=lambda e: button.config(bg=OPTION_COLOR))

if __name__ == "__main__":
    main_menu()
    root.mainloop()