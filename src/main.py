from tkinter import *
import json
import random

from util import *
from bank import question_bank

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
                           command=lambda: end_exam(question_details_dict))
    end_exam_button.bind("<Enter>", func=lambda e: on_enter_option(end_exam_button))
    end_exam_button.bind("<Leave>", func=lambda e: on_leave_option(end_exam_button))
    end_exam_button.pack(side=RIGHT,
                         padx=(0, 15))
    
    def end_exam(question_details_dict: dict) -> None:
        end_exam_button.config(text="EXIT",
                               padx=3,
                               command=lambda: exam_window.destroy())
        """
        Ends the exam and scans through the user's selected answers,
        marking correct or incorrect.
        """
        
        # iterates through the question details
        for value in question_details_dict.values():
            # if the user's selected answer is correct
            if value["selected_answer"] == value["answer"]:
                # change the button's color to green
                value["button"].config(fg="#3cd470")
            # if the user's selected answer is incorrect
            else:
                # change the button's color to red
                value["button"].config(fg="#cd4545")     
    
    flag_button = Util.button(question_details_frame)
    flag_button.config(text="⚐",
                       padx=5,
                       pady=0,
                       command=lambda: update_question_navigator_icon("flag",
                                                                      question_details_dict))
    flag_button.bind("<Enter>", func=lambda e: on_enter_option(flag_button))
    flag_button.bind("<Leave>", func=lambda e: on_leave_option(flag_button))
    flag_button.pack(side=RIGHT,
                     padx=(0, 15))
    
    # displays the timer
    timer_label = Util.label(question_details_frame)
    timer_label.config(text="00:00:00",
                       bg=DETAILS_BG_COLOR)
    timer_label.pack(side=RIGHT,
                     padx=(0, 358))
    
    question_details_frame.pack(side=TOP,
                                fill=BOTH,)
    
    # goes to previous question
    prev_button = Util.button(exam_window)
    prev_button.config(text="<",
                       padx=10,
                       pady=5,
                       command=lambda: display_current_question("prev",
                                                                question_number_label,
                                                                current_question_label,
                                                                current_choice_frame,
                                                                question_details_dict))
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
                                                                current_question_label,
                                                                current_choice_frame,
                                                                question_details_dict))
    next_button.bind("<Enter>", func=lambda e: on_enter_option(next_button))
    next_button.bind("<Leave>", func=lambda e: on_leave_option(next_button))
    next_button.pack(side=RIGHT,
                     padx=(0, 15))
    
    # list of randomly selected questions
    chosen_questions_list = create_questions()
    
    # question navigator frame
    question_navigator_frame = Util.frame(exam_window)
    
    question_details_dict = {}
    # creates "i" amount of question navigator buttons
    for i in range(1, 31):
        # populates the dictionary
        # with each key representing the question number
        # and its associated information
        question_details_dict.update({
            str(i): {
                "button": None,
                "icon": None,
                "is_flagged": False,
                "question": None,
                "answer": None,
                "format": None,
                "choices": [],
                
                "selected_answer": None,
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
                                                                                      current_question_label,
                                                                                      current_choice_frame,
                                                                                      question_details_dict))
            
        # binds each button to a hover effect
        question_navigator_button.bind("<Enter>", lambda e, button=question_navigator_button: on_enter_question_navigator(button))
        question_navigator_button.bind("<Leave>", lambda e, button=question_navigator_button: on_leave_question_navigator(button))
        question_navigator_button.pack(side=LEFT)
        
        question_navigator = question_details_dict[str(i)]
        
        # button widget
        question_navigator["button"] = question_navigator_button
        # the button's text (or state)
        question_navigator["icon"] = question_navigator_button.cget("text")
        # question
        question_navigator["question"] = chosen_questions_list[i - 1][0]
        # question's answer
        question_navigator["answer"] = chosen_questions_list[i - 1][1]
        # question's format
        # (multiple choice, select one, etc.)
        question_navigator["format"] = chosen_questions_list[i - 1][2]
        # question's choices
        question_navigator["choices"] = chosen_questions_list[i - 1][3]
        
        # if it is the first idx
        if i == 1:
            # change the first button's icon to "⭗" (current)
            question_navigator_button.config(text="⭗")
    
    # displays current question
    current_question_label = Util.label(exam_window)
    # selects the first question
    current_question_label.config(text=question_details_dict["1"]["question"])
    current_question_label.pack(expand=True,
                                fill="none")
    
    # displays the current choices
    current_choice_frame = Util.frame(exam_window)
    create_choices(current_choice_frame, question_details_dict)
    current_choice_frame.pack(expand=True,
                              fill="none",)
    
    def on_enter_question_navigator(button) -> None:
        """
        Changes the button texture
        when hovering over the button.
        """

        # saves the current text
        current_text = button.cget("text")
        button.original_text = current_text
        
        # if the current text matches, configure to its
        # respective opposite symbol
        if current_text == "⭘":
            button.config(text="⭗")
        elif current_text == "⏺":
            button.config(text="⦿")
        elif current_text == "⚐":
            button.config(text="⚑")
    
    def on_leave_question_navigator(button) -> None:
        """
        Changes the button texture
        when no longer hovering over the button.
        """
        
        # iterates through the question navigator dict
        # to find the question number (key) and button (value)
        for key, value in question_details_dict.items():
            # if user is currently on the question of the button
            if int(key) == current_question_idx:
                # assign the button as the current button
                current_button = value["button"]

        # if the button does not equal to the current button
        # (meaning if the user is currently not on **that** question)
        if button != current_button:
            # restore it's original text
            button.config(text=button.original_text)
        
    question_navigator_frame.pack(side=BOTTOM,
                                  pady=(0, 20),)

def create_questions() -> list:
    """
    Creates a list of randomly selected questions
    to be displayed in the exam.
    """
    
    with open("data.json", "r") as file:
        data = json.load(file)
    
    questions_to_be_chosen = []
    # selects 30 random questions;
    # questions not selected before will have a higher
    # chance to be selected now
    for i in range(30):
        # TODO: what if question is blank
        
        # selects a random question
        module_chosen = random.choice(list(question_bank.keys()))
        tag_chosen = random.choice(list(question_bank[module_chosen].keys()))
        question_chosen = random.choice(list(data["bank"][module_chosen][tag_chosen]["questions"]))
        
        result_chosen = question_bank[module_chosen][tag_chosen][question_chosen]
        
        # if the question has a function
        if result_chosen.get("function"):
            # randomize the choices
            result_choices = result_chosen["function"]()
        
        # adds the question to the list of questions to be chosen
        questions_to_be_chosen.append([
            result_chosen["question"],
            result_chosen["answer"],
            result_chosen["format"],
            result_choices,
        ])
        # shuffles the list
        random.shuffle(questions_to_be_chosen)
    
    return questions_to_be_chosen

def create_choices(current_choice_frame: Frame,
                   question_details_dict: dict) -> None:
    """
    Creates the question's choices
    in the respective format.
    """
    
    current_question = question_details_dict[str(current_question_idx)]

    choice_format = current_question["format"]
    # if the current question's format is radiobutton
    if choice_format == "radio":
        # to display on the left side
        radiobutton_left_frame = Util.frame(current_choice_frame)
        # to display on the right side
        radiobutton_right_frame = Util.frame(current_choice_frame)
        
        option = StringVar()
        for idx, choice in enumerate(current_question["choices"]):
            # if to be displayed on the left side
            if idx <= 1:
                radiobutton = Util.radiobutton(radiobutton_left_frame)
            # if to be displayed on the right side
            elif idx >= 2:
                radiobutton = Util.radiobutton(radiobutton_right_frame)
                
            radiobutton.config(text=choice,
                               value=choice,
                               variable=option,
                               command=lambda: on_update_selected_answer(option.get()))
            radiobutton.pack(anchor=W)
        
        # if an answer was selected before (and user selects a different question)
        if current_question["selected_answer"] != None:
            # preselect the saved answer (when user revisits the question)
            option.set(current_question["selected_answer"])
        
        radiobutton_left_frame.pack(side=LEFT,
                                    anchor=W,
                                    padx=(0, 350),)
        radiobutton_right_frame.pack(anchor=W,)
    
    def on_update_selected_answer(answer) -> None:
        """
        Updates the question navigator dictionary's selected answer
        to allow the user to save its work if they choose to
        navigate to a different question.
        """
        
        current_question["selected_answer"] = answer
        update_question_navigator_icon("complete", question_details_dict)

def display_current_question(action: str,
                             question_number_label: Label,
                             current_question_label: Label,
                             current_choice_frame: Frame,
                             question_details_dict: dict) -> None:
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
    
    # resets all the question navigator buttons to its previous state
    for value in question_details_dict.values():
        # if the question is not flagged
        if value["is_flagged"] == False:
            value["button"].config(text=value["icon"])
        # otherwise
        else:
            value["button"].config(text="⚐")
    
    current_question = question_details_dict[str(current_question_idx)]
    button = current_question["button"]
    icon = button.cget("text")
    
    # if the current text matches, configure to its
    # respective opposite symbol
    if icon == "⭘":
        button.config(text="⭗")
    elif icon == "⏺":
        button.config(text="⦿")
    elif icon == "⚐":
        button.config(text="⚑")
    
    # removes any current choices displayed on screen
    for choice in current_choice_frame.winfo_children():
        choice.destroy()
    
    # updates to current question information
    create_choices(current_choice_frame, question_details_dict)
    current_question_label.config(text=current_question["question"])
    question_number_label.config(text=f"Question {current_question_idx}")

def update_question_navigator_icon(action: str,
                                   question_details_dict: dict=None) -> None:
    """
    Updates the question navigator icon
    in accordance the current question state
    (ex. current, complete, flagged)
    """
    
    current_question = question_details_dict[str(current_question_idx)]
    
    # if flagging a question
    if action == "flag":
        # if it is not flagged yet
        if current_question["button"].cget("text") != "⚑":
            # change button's text to a flag
            current_question["button"].config(text="⚑")
            # sets flag status to true
            current_question["is_flagged"] = True
        # if it is already flagged
        # (user wants to unflag question)
        else:
            # revert button's text to previous state
            if current_question["icon"] == "⏺":
                current_question["button"].config(text="⦿")
            elif current_question["icon"] == "⭘":
                current_question["button"].config(text="⭗")
                
            # sets flag status to false
            current_question["is_flagged"] = False
    # if a question has an answer selected
    elif action == "complete":
        # set the current button text to "complete"
        current_question["icon"] = "⏺"
        
        # if the current question is not flagged
        if current_question["button"].cget("text") != "⚑":
            # set the current question button's text
            # to the "selected and completed" symbol
            current_question["button"].config(text="⦿")

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