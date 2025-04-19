from tkinter import *
from tkinter import font
import json
import random

from util import *
from bank import question_bank, \
    MULTIPLE_CHOICE, TRUE_OR_FALSE, FREE_RESPONSE, SELECT_THAT_APPLY, MATCH_TO_ANSWER

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
        
        with open("data.json", "r") as file:
            data = json.load(file)
        
        # if there are questions marked wrong
        if len(data["questions_marked_wrong"]) > 0:
            for question in data["questions_marked_wrong"]:
                count = question[3]
                
                # decrement the count by one
                if count > 0:
                    count -= 1
        
        # iterates through the question details
        for value in question_details_dict.values():
            question_location = value["location"]
            module = question_location[0]
            tag = question_location[1]
            question = question_location[2]
            
            # displays the correct answer for post-exam viewing
            value["is_end"] = True
            
            # if the user's selected answer is correct
            if value["selected_answer"] == value["answer"]:
                # change the button's color to green
                value["button"].config(fg="#3cd470")
                
                # increment the amount of times the question was answered correctly
                # to decrease the chances of seeing the question again
                data["bank"][module][tag]["questions"][question] += 1
            # if the user's selected answer is incorrect
            else:
                # change the button's color to red
                value["button"].config(fg="#cd4545")
                
                # add the question to a list of questions answered incorrectly
                # with a random counter that will countdown on
                # when the question will appear in the next exam
                data["questions_marked_wrong"].append(question_location + [random.randint(1, 3)])
        
        with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))
        
        # reloads the current question display
        display_current_question(current_question_idx,
                                 question_number_label,
                                 current_question_label,
                                 current_choice_frame,
                                 current_answer_label,
                                 question_details_dict,)
    
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
                                                                current_answer_label,
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
                                                                current_answer_label,
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
                
                "location": None,
                "question": None,
                "answer": None,
                "format": None,
                "choices": [],
                
                "selected_answer": None,
                "is_end": False,
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
                                                                                      current_answer_label,
                                                                                      question_details_dict))
            
        # binds each button to a hover effect
        question_navigator_button.bind("<Enter>", lambda e, button=question_navigator_button: on_enter_question_navigator(button))
        question_navigator_button.bind("<Leave>", lambda e, button=question_navigator_button: on_leave_question_navigator(button))
        question_navigator_button.pack(side=LEFT)
        
        question_details = question_details_dict[str(i)]
        
        # button widget
        question_details["button"] = question_navigator_button
        # the button's text (or state)
        question_details["icon"] = question_navigator_button.cget("text")
        
        # question's location (for easier access)
        question_details["location"] = chosen_questions_list[i - 1][0]
        # question
        question_details["question"] = chosen_questions_list[i - 1][1]
        # question's answer
        question_details["answer"] = chosen_questions_list[i - 1][2]
        # question's format
        # (multiple choice, select one, etc.)
        question_details["format"] = chosen_questions_list[i - 1][3]
        # question's choices
        question_details["choices"] = chosen_questions_list[i - 1][4]
        
        # if the question format is "select that apply"
        if question_details["format"] == SELECT_THAT_APPLY:
            # initialize a set
            question_details["selected_answer"] = set()
        # if the question format is "match to answer"
        elif question_details["format"] == MATCH_TO_ANSWER:
            # initialize a list
            question_details["selected_answer"] = list()
        
        # if it is the first idx
        if i == 1:
            # change the first button's icon to "⭗" (current)
            question_navigator_button.config(text="⭗")
    
    # displays current question
    current_question_label = Util.label(exam_window)
    current_question_label.pack(expand=True,
                                fill="none")
    
    # displays the current choices
    current_choice_frame = Util.frame(exam_window)
    current_choice_frame.pack(expand=True,
                              fill="none",)
    
    # displays the current answer (initially hidden until post-exam)
    italic_font = font.Font(family="Arial", size=15, slant="italic")
    current_answer_label = Util.label(exam_window)
    current_answer_label.config(text="",
                                font=italic_font,
                                wraplength=900,)
    current_answer_label.pack(pady=5)
    
    # displays the first question and choices
    display_current_question(str(1),
                             question_number_label,
                             current_question_label,
                             current_choice_frame,
                             current_answer_label,
                             question_details_dict)
    
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
        # TODO: what if question/answer is blank
        # TODO: add questions marked wrong first
        
        # selects a random question
        module_chosen = random.choice(list(question_bank.keys()))
        tag_chosen = random.choice(list(question_bank[module_chosen].keys()))
        # TODO: prioritize questions that have not been chosen frequently
        question_chosen = random.choice(list(data["bank"][module_chosen][tag_chosen]["questions"]))
        
        question_location = [module_chosen, tag_chosen, question_chosen]
        result_chosen = question_bank[module_chosen][tag_chosen][question_chosen]
        details_chosen = result_chosen["details"]
        format_chosen = result_chosen["format"]
        
        details_to_be_chosen = [
            key for key in details_chosen.keys()
        ]
        question_chosen = random.choice(details_to_be_chosen)
        correct_answer = details_chosen[question_chosen]
        
        # if the question format is multiple choice
        if format_chosen == MULTIPLE_CHOICE:
            # creates a list of incorrect choices to be chosen
            # excluding the correct answer
            choices_chosen = [
                choice for choice in details_chosen.values()
            ]
            random.shuffle(choices_chosen)
        # if the question format is a select that apply
        elif format_chosen == SELECT_THAT_APPLY:
            # reassigns the single correct answer to multiple correct answers
            correct_answer = details_chosen[question_chosen][0]
            
            # creates a list of incorrect choices
            choices_chosen = [
                choice for choice in details_chosen[question_chosen][1]
            ]
            # combines the correct answer with the incorrect choices
            choices_chosen = correct_answer + choices_chosen
            random.shuffle(choices_chosen)
            
            # converts list into set (for exam grading purpose)
            correct_answer = set(correct_answer)
        # if the question format is a match to answer
        elif format_chosen == MATCH_TO_ANSWER:
            question_chosen_list = []
            correct_answer = [] # reassign the single correct answer to a list of correct answers
            choices_chosen = []
            
            # TODO: option to randomize subquestions
            
            # iterate the amount of sub-questions/answer
            for i in range(len(details_chosen[question_chosen])):
                subquestion = details_chosen[question_chosen][i][0]
                answer = details_chosen[question_chosen][i][1]
                
                # adds the subquestion
                question_chosen_list.append(subquestion)
                # adds the correct answer (in order)
                correct_answer.append(answer)
                # adds the choice (to later be shuffled)
                choices_chosen.append(answer)
            
            question_chosen = [question_chosen] + question_chosen_list
            random.shuffle(choices_chosen)
        # if the question format is true or false
        elif format_chosen == TRUE_OR_FALSE:
            choices_chosen = ["True", "False"]
        # if the question format is free response
        elif format_chosen == FREE_RESPONSE:
            choices_chosen = None
        
        # adds the question to the list of questions to be chosen
        questions_to_be_chosen.append([
            question_location,
            
            question_chosen,
            correct_answer,
            format_chosen,
            choices_chosen,
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
    
    def on_update_selected_answer(selected_answer) -> None:
        """
        Updates the question navigator dictionary's selected answer
        to allow the user to save its work if they choose to
        navigate to a different question.
        """

        # saves the selected answer
        current_question["selected_answer"] = selected_answer
        
        # if the selected answer is empty
        # (because user may have deselected/deleted their previous selected answer)
        if (selected_answer == ""
            or len(selected_answer) <= 0
            or (isinstance(selected_answer, list) and "" in selected_answer)):
            # update the question navigator to "incomplete" icon
            update_question_navigator_icon("incomplete", question_details_dict)
        # if there is a selected answer
        else:
            # update the question navifator to "complete" icon
            update_question_navigator_icon("complete", question_details_dict)

    choice_format = current_question["format"]
    # if the question is multiple choice, or true or false
    if choice_format == MULTIPLE_CHOICE or choice_format == TRUE_OR_FALSE:
        # to display on the left side
        radiobutton_left_frame = Util.frame(current_choice_frame)
        # to display on the right side
        radiobutton_right_frame = Util.frame(current_choice_frame)
        
        # if it's a multiple choice question
        if choice_format == MULTIPLE_CHOICE:
            # align the choices with two answers on the left
            # and two answers on the right
            left_frame_target_idx = 1
            right_frame_target_idx = 2
        # if it's a true or false question
        elif choice_format == TRUE_OR_FALSE:
            # align the choices with one answer on the left
            # and one answer on the right
            left_frame_target_idx = 0
            right_frame_target_idx = 1
        
        option = StringVar()
        for idx, choice in enumerate(current_question["choices"]):
            # if to be displayed on the left side
            if idx <= left_frame_target_idx:
                radiobutton = Util.radiobutton(radiobutton_left_frame)
            # if to be displayed on the right side
            elif idx >= right_frame_target_idx:
                radiobutton = Util.radiobutton(radiobutton_right_frame)
                
            radiobutton.config(text=choice,
                               value=choice,
                               variable=option,
                               command=lambda: on_update_selected_answer(option.get()))
            radiobutton.pack(anchor=W)
        
        radiobutton_left_frame.pack(side=LEFT,
                                    anchor=W,
                                    padx=(0, 350),)
        radiobutton_right_frame.pack(anchor=W,)
    # if the question is a select that apply
    elif choice_format == SELECT_THAT_APPLY:
        # any previous answers selected before are reselected
        selected_checkbox = current_question["selected_answer"]
        
        # iterates through the randomize choices
        for choice in current_question["choices"]:
            option = StringVar(value=f"-{choice}")

            checkbox = Util.checkbox(current_choice_frame)
            checkbox.config(text=f"{choice}{" " * (115 - len(choice))}", # " " for better alignment
                            onvalue=choice,
                            offvalue=f"-{choice}",
                            variable=option,
                            command=lambda o=option: on_update_selected_checkbox(o.get()))
            checkbox.pack(anchor=W)
            
            # if an answer has been previously selected, then reselect the checkbox
            # (for if user leaves the question and comes back later)
            if choice in selected_checkbox:
                checkbox.select()
        
        def on_update_selected_checkbox(selected_answer: str) -> None:
            """
            Updates the list of currently selected checkboxes
            and saves the answer.
            """
            
            # if starts with a "-" (user wants to deselect their answer)
            if selected_answer.startswith("-"):
                # remove the answer
                selected_checkbox.remove(selected_answer[1:])
            # otherwise
            else:
                # add the answer
                selected_checkbox.add(selected_answer)
                
            on_update_selected_answer(selected_checkbox)
    # if the question is a match to answer
    elif choice_format == MATCH_TO_ANSWER:
        # reassigns any previous answer that user may have saved
        selected_optionmenu = current_question["selected_answer"]
        
        # if the list is empty
        if len(selected_optionmenu) <= 0:
            # populate the list with placeholders (to later be indexed)
            selected_optionmenu = [""] * len(current_question["choices"])
        
        # iterates through the list of questions, skipping the first idx
        # (first idx contains the main question, and every idx afterwards
        # is the subquestion)
        for i in range(1, len(current_question["question"])):
            optionmenu_frame = Util.frame(current_choice_frame)
            optionmenu_frame.pack()
            
            # displays the subquestion
            subquestion_label = Util.label(optionmenu_frame)
            subquestion_label.config(text=current_question["question"][i],
                                     width=50,
                                     wraplength=600,
                                     anchor=W,
                                     justify=LEFT,)
            subquestion_label.pack(side=LEFT,)
            
            # displays the optionmenu
            option = StringVar(value=selected_optionmenu[i - 1])
            optionmenu = Util.optionmenu(optionmenu_frame,
                                         option,
                                         *current_question["choices"],
                                         func=lambda e, idx=i: on_update_selected_optionmenu(e, idx - 1))
            
            # if this is the last optionmenu
            if i == (len(current_question["question"]) - 1):
                # do not add padding
                optionmenu.pack()
            else:
                optionmenu.pack(pady=(0,25))
        
        # fixes visual bug;
        # creates the last optionmenu (to allow for the bugged text to print),
        # then destroys itself
        option = StringVar(value="")
        last_optionmenu = Util.optionmenu(optionmenu_frame,
                                          option,
                                          *current_question["choices"],)
        last_optionmenu.pack()
        last_optionmenu.destroy()
            
        def on_update_selected_optionmenu(selected_answer: str,
                                          idx: int,) -> None:
            """
            Updates the list of currently selected optionmenu
            and saves the answer.
            """
            
            # replaces with an answer at specified idx
            # (this allows the answer to remain in order for exam grading)
            selected_optionmenu[idx] = selected_answer

            on_update_selected_answer(selected_optionmenu)
    # if the question is free response
    elif choice_format == FREE_RESPONSE:
        option = StringVar()
        
        entrybox = Util.entry(current_choice_frame)
        entrybox.config(textvariable=option)
        # calls the function (passing the current entrybox text)
        # every time the user enters a text in the entrybox
        option.trace_add("write", lambda *args: on_update_selected_answer(option.get()))
        entrybox.pack()
    
    # if an answer was selected before (and user selects a different question)
    # and the choice format is not "select that apply" format
    if current_question["selected_answer"] and choice_format != SELECT_THAT_APPLY:
        # preselect the saved answer (when user revisits the question)
        option.set(current_question["selected_answer"])

def display_current_question(action: str,
                             question_number_label: Label,
                             current_question_label: Label,
                             current_choice_frame: Frame,
                             current_answer_label: Label,
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
    
    # if user is currently in post-exam viewing
    if current_question["is_end"] == True:
        current_answer = current_question["answer"]
        
        # if the current answer is a list or a set
        if (isinstance(current_answer, list)
            or isinstance(current_answer, set)):
            current_answer_to_iterate = current_answer
            current_answer = "" # reassign the current answer (to later be displayed)

            # labels a number for each answer
            # (ex. [1] some answer)
            for idx, answer in enumerate(current_answer_to_iterate):
                current_answer += "[" + str(idx + 1) + "] " + answer + " "
        
        # display the correct answer
        current_answer_label.config(text=current_answer)
    
    # if the question format is match to answer,
    # then the value is a list
    if current_question["format"] == MATCH_TO_ANSWER:
        # displays the first idx of the list (which is the actual question)
        current_question_label.config(text=current_question["question"][0])
    # otherwise, then the value is not a list (it's a string)
    else:
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
    # if a question has not been selected
    # (user may have deselected/deleted the answer)
    elif action == "incomplete":
        # set the current button text to "incomplete"
        current_question["icon"] = "⭘"
        
        # if the current question is not flagged
        if current_question["button"].cget("text") != "⚑":
            # set the current question button's text
            # to the "selected and incompleted" symbol
            current_question["button"].config(text="⭗")

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
    
    # resets file
    with open("data.json", "r") as file:
        data = json.load(file)
    
    data["questions_marked_wrong"].clear()
    
    with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))