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
    create_button.bind("<Enter>", func=lambda e: on_enter_option(create_button))
    create_button.bind("<Leave>", func=lambda e: on_leave_option(create_button))
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
    exam_window.geometry("1075x800")
    exam_window.config(background=BG_COLOR)
    
    # question details frame
    question_details_frame = Util.frame(exam_window)
    question_details_frame.config(bg=DETAILS_BG_COLOR,
                                      pady=10,)
    
    # displays the current question number
    question_number_label = Util.label(question_details_frame)
    question_number_label.config(text=f"Question {current_question_idx}",
                                 bg=DETAILS_BG_COLOR,)
    question_number_label.pack(side=LEFT,
                               padx=(15, 0))
    
    # ends the exam
    end_exam_button = Util.button(question_details_frame)
    end_exam_button.config(text="END",
                           padx=5,
                           pady=0,
                           command=lambda: print("exit"))
    end_exam_button.bind("<Enter>", func=lambda e: on_enter_option(end_exam_button))
    end_exam_button.bind("<Leave>", func=lambda e: on_leave_option(end_exam_button))
    end_exam_button.pack(side=RIGHT,
                         padx=(0, 15))
    
    flag_button = Util.button(question_details_frame)
    flag_button.config(text="⚐",
                       padx=5,
                       pady=0,
                       command=lambda: update_question_navigator_icon("flag",
                                                                      question_navigator_dict))
    flag_button.bind("<Enter>", func=lambda e: on_enter_option(flag_button))
    flag_button.bind("<Leave>", func=lambda e: on_leave_option(flag_button))
    flag_button.pack(side=RIGHT,
                     padx=(0, 15))
    
    # displays the timer
    timer_label = Util.label(question_details_frame)
    timer_label.config(text="00:00",
                       bg=DETAILS_BG_COLOR)
    timer_label.pack(side=RIGHT,
                     padx=(0, 375))
    
    question_details_frame.pack(side=TOP,
                                    fill=BOTH,)
    
    # goes to previous question
    prev_button = Util.button(exam_window)
    prev_button.config(text="<",
                       padx=10,
                       pady=5,
                       command=lambda: display_current_question("prev",
                                                                question_number_label,
                                                                question_navigator_dict))
    prev_button.bind("<Enter>", func=lambda e: on_enter_option(prev_button))
    prev_button.bind("<Leave>", func=lambda e: on_leave_option(prev_button))
    prev_button.pack(side=LEFT,
                     padx=(15, 0))
    
    # goes to next question
    next_button = Util.button(exam_window)
    next_button.config(text=">",
                       padx=10,
                       pady=5,
                       command=lambda: display_current_question("next",
                                                                question_number_label,
                                                                question_navigator_dict))
    next_button.bind("<Enter>", func=lambda e: on_enter_option(next_button))
    next_button.bind("<Leave>", func=lambda e: on_leave_option(next_button))
    next_button.pack(side=RIGHT,
                     padx=(0, 15))
    
    # displays current question
    current_question_label = Util.label(exam_window)
    current_question_label.config(text="current question")
    current_question_label.pack(side=TOP)
    
    # question navigator frame
    question_navigator_frame = Util.frame(exam_window)
    
    #TODO: ⏺
    
    question_navigator_dict = {}
    # creates "i" amount of question navigator buttons
    for i in range(1, 31):
        # populates the dictionary
        # with each key representing the question number
        # and its associated button widget and button's text
        question_navigator_dict.update({
            str(i): {
                "button": None,
                "text": None,
                "is_flagged": False,
            },
        })
        
        # allows to navigate to different questions
        question_navigator_button = Util.button(question_navigator_frame)
        question_navigator_button.config(text="⭘",
                                         font=(FONT, 15, "normal"),
                                         bg=BG_COLOR,
                                         activebackground=BG_COLOR,
                                         padx=0,
                                         pady=0,
                                         relief=FLAT,
                                         bd=0,
                                         command=lambda i=i: display_current_question(str(i),
                                                                                      question_number_label,
                                                                                      question_navigator_dict))
            
        # binds each button to a hover effect
        question_navigator_button.bind("<Enter>", lambda e, button=question_navigator_button: on_enter_question_navigator(button))
        question_navigator_button.bind("<Leave>", lambda e, button=question_navigator_button: on_leave_question_navigator(button))
        question_navigator_button.pack(side=LEFT)
        
        # button widget
        question_navigator_dict[str(i)]["button"] = question_navigator_button
        # the button's text
        question_navigator_dict[str(i)]["text"] = question_navigator_button.cget("text")
        
        # if it is the first idx
        if i == 1:
            # change the first button's texture to "⭗" (current)
            question_navigator_button.config(text="⭗")
        
    def on_enter_question_navigator(button) -> None:
        """
        Changes the button texture
        when hovering over the button.
        """

        # saves the current text
        current_text = button.cget("text")
        button.original_text = current_text
        
        if current_text == "⭘":
            button.config(text="⭗")
        elif current_text == "⚐":
            button.config(text="⚑")
    
    def on_leave_question_navigator(button) -> None:
        """
        Changes the button texture
        when no longer hovering over the button.
        """
        
        # iterates through the question navigator dict
        # to find the question number (key) and button (value)
        for key, value in question_navigator_dict.items():
            # if user is currently on the question of the button
            if int(key) == current_question_idx:
                # assign the button as the current button
                current_button = value["button"]

        # if the button does not equal to the current button
        if button != current_button:
            # restore it's original text
            button.config(text=button.original_text)
        
    question_navigator_frame.pack(side=BOTTOM,
                                  pady=(0, 20),)

def display_current_question(action: str, question_number_label: Label, question_navigator_dict: dict) -> None:
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
    
    # resets all the question navigator buttons to its previous state
    for value in question_navigator_dict.values():
        # if the question is not flagged
        if value["is_flagged"] == False:
            value["button"].config(text=value["text"])
        # otherwise
        else:
            value["button"].config(text="⚐")
    
    button = question_navigator_dict[str(current_question_idx)]["button"]
    
    # if the current button is flagged
    if button.cget("text") == "⚐":
        button.config(text="⚑")
    # otherwise
    else:
        button.config(text="⭗")
    
    # if attempting to navigate past the maximum questions
    if current_question_idx > 30:
        # loop back to the first question
        current_question_idx = 1
    # if attempting to navigate below the minimum questions
    elif current_question_idx < 1:
        # loop back to the last question
        current_question_idx = 30
        
    # TODO: display question and choices
        
    # updates display information
    question_number_label.config(text=f"Question {current_question_idx}")

def update_question_navigator_icon(action: str, question_navigator_dict: dict=None) -> None:
    """
    Updates the question navigator icon
    in accordance the current question state
    (ex. current, complete, flagged)
    """
    
    button = question_navigator_dict[str(current_question_idx)]["button"]
    text = question_navigator_dict[str(current_question_idx)]["text"]
    
    # if flagging a question
    if action == "flag":
        # if it is not flagged yet
        if button.cget("text") != "⚑":
            # change button's text to a flag
            button.config(text="⚑")
            # sets flag status to true
            question_navigator_dict[str(current_question_idx)]["is_flagged"] = True
        # if it is already flagged
        # (user wants to unflag question)
        else:
            # revert button's text to previous state
            button.config(text=text)
            # sets flag status to false
            question_navigator_dict[str(current_question_idx)]["is_flagged"] = False

def on_enter_option(button) -> None:
    """
    Changes the button texture
    when hovering over the button.
    """

    button.config(bg=HOVER_COLOR)

def on_leave_option(button) -> None:
    """
    Changes the button texture
    when no longer hovering over the button.
    """

    button.config(bg=OPTION_COLOR)

if __name__ == "__main__":
    main_menu()
    root.mainloop()