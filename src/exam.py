from tkinter import *
from tkinter import font
import json
import random

from util import *
from bank import Bank, question_bank, \
    MULTIPLE_CHOICE, TRUE_OR_FALSE, FREE_RESPONSE, SELECT_THAT_APPLY, MATCH_TO_ANSWER, MATCH_TO_ANSWER_RANDOMIZED

def create_exam() -> None:
    """
    Displays exam GUI.
    """

    global current_question_idx
    
    current_question_idx = 1
    
    # creates a new window (for the exam)
    exam_window = Toplevel()  
    exam_window.geometry("1075x800")
    exam_window.resizable(False, False)
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
    
    # TODO: add a confirmation to ending exam
    
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
                
                # decrement the count by one
                question[1] -= 1
                
                # if the count is <= 0
                if question[1] <= 0:
                    redemption_question_idx = data["questions_marked_wrong"].index(question)
                    # remove the question from the list
                    redemption_question = data["questions_marked_wrong"].pop(redemption_question_idx)
                    # and add it into the 'redemption questions' list
                    # where the question will now be prioritize to be chosen first
                    data["redemption_questions"].append(redemption_question)
        
        # iterates through the question details
        for value in question_details_dict.values():
            question_location = value["location"]
            module = question_location[0]
            tag = question_location[1]
            question = question_location[2]
            
            # displays the correct answer for post-exam viewing
            value["is_end"] = True
            
            # if the user's selected answer is correct
            if (value["selected_answer"] == value["answer"]
                or (isinstance(value["selected_answer"], str)
                and value["selected_answer"].lower() == value["answer"].lower())):
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
                data["questions_marked_wrong"].append([question_location] + [random.randint(1, 3)])
        
        # checks if all the questions in each tag have been marked correctly
        # to decrease the chances of seeing questions from *this* tag
        for module in data["bank"]:
            for tag in data["bank"][module]:
                question_count = []
                # iterates the count of each question
                for count in data["bank"][module][tag]["questions"].values():
                    question_count.append(count)
                
                # if the overall tag count is less than the smallest question count,
                if data["bank"][module][tag]["count"] < min(question_count):
                    # then increment the tag count
                    data["bank"][module][tag]["count"] += 1
        
        with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))
        
        # reloads the current question display
        display_current_question(current_question_idx,
                                 question_number_label,
                                 current_question_label,
                                 current_choice_frame,
                                 current_answer_label,
                                 question_details_dict,
                                 maximum_number_of_questions,)
    
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

    def exam_timer(hour: int, minute: int, second: int,) -> None:
        """
        Exam timer that increments every second.
        """
        
        second += 1
        
        # if 60 seconds has passed
        if second >= 60:
            # add a minute and reset the seconds
            minute += 1
            second = 0
        # if 60 minutes has passed
        if minute >= 60:
            # add an hour and reset the minutes
            hour += 1
            minute = 0
        
        # if the value is a single digit
        if second <= 9:
            # add zero-padding
            second_label = "0" + str(second)
        # otherwise,
        elif second >= 10:
            # display the value
            second_label = str(second)
        if minute <= 9:
            minute_label = "0" + str(minute)
        elif minute >= 10:
            minute_label = str(minute)
        if hour <= 9:
            hour_label = "0" + str(hour)
        elif hour >= 10:
            hour_label = str(hour)
            
        # if it is under the maximum time limit
        # and the exam window is still opened
        if (hour <= 59 and minute <= 59 and second <= 59
            and exam_window.winfo_exists()):
            timer_label.config(text=f"{hour_label}:{minute_label}:{second_label}")
            exam_window.after(1000, exam_timer, hour, minute, second)
    
    # start timer at specified time (hour, minute, second)
    exam_timer(0, 0, 0)
    
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
                                                                question_details_dict,
                                                                maximum_number_of_questions,))
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
                                                                question_details_dict,
                                                                maximum_number_of_questions,))
    next_button.bind("<Enter>", func=lambda e: on_enter_option(next_button))
    next_button.bind("<Leave>", func=lambda e: on_leave_option(next_button))
    next_button.pack(side=RIGHT,
                     padx=(0, 15))
    
    # list of randomly selected questions
    chosen_questions_list, maximum_number_of_questions = create_questions()
    
    # question navigator frame
    question_navigator_frame = Util.frame(exam_window)
    
    question_details_dict = {}
    # creates "i" amount of question navigator buttons
    for i in range(1, maximum_number_of_questions + 1):
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
                                                                                      question_details_dict,
                                                                                      maximum_number_of_questions,))
            
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
        # if the question format is "match to answer" or "match to answer randomized"
        elif question_details["format"] == MATCH_TO_ANSWER or question_details["format"] == MATCH_TO_ANSWER_RANDOMIZED:
            # initialize a list
            question_details["selected_answer"] = list()
        
        # if it is the first idx
        if i == 1:
            # change the first button's icon to "⭗" (current)
            question_navigator_button.config(text="⭗")
    
    # displays current question
    current_question_label = Util.label(exam_window)
    current_question_label.config(wraplength=900,)
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
                             question_details_dict,
                             maximum_number_of_questions)
    
    def on_enter_question_navigator(button: Button) -> None:
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
    
    def on_leave_question_navigator(button: Button) -> None:
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

def create_questions():
    """
    Creates a list of randomly selected questions
    to be displayed in the exam.
    """
    
    with open("data.json", "r") as file:
        data = json.load(file)
        
    current_modules_selected = []
    current_tags_selected = []
    total_number_of_questions = []
    # creates a list of modules selected   
    for module in data["questions_selected"]:
        if len(data["questions_selected"][module]) > 0:
            current_modules_selected.append(module)
            # creates a list of tags selected
            for tag in data["questions_selected"][module]:
                current_tags_selected.append(tag)
                # creates a list of all the questions (within the module and tag)
                # to later be counted
                for question in question_bank[module][tag]:
                    total_number_of_questions.append(question)
                    
    # the number of questions - the number of questions marked wrong
    maximum_number_of_questions = len(total_number_of_questions) - len(data["questions_marked_wrong"])
    
    # TODO: add an error if there are no available questions to be selected
    
    # if the maximum number is greater than 30, or there is a question already preselected
    if maximum_number_of_questions >= 30 or "" not in data["debug_question"]:
        # set to 30
        maximum_number_of_questions = 30

    questions_to_be_chosen_final = []
    module_idx = 0
    # repeats until the maximum_number_of_questions are selected
    while len(questions_to_be_chosen_final) < maximum_number_of_questions:
        with open("data.json", "r") as file:
            data = json.load(file)
        
        # if there is a question already preselected,
        # then select that question (used for debugging purposes)
        if "" not in data["debug_question"]:
            module_chosen = data["debug_question"][0]
            tag_chosen = data["debug_question"][1]
            question_chosen = data["debug_question"][2]
        # if there are redemption questions,
        # then start picking questions from the redemption questions list
        elif len(data["redemption_questions"]) > 0:
            redemption_question = data["redemption_questions"].pop()
            module_chosen = redemption_question[0][0]
            tag_chosen = redemption_question[0][1]
            question_chosen = redemption_question[0][2]
            
            with open("data.json", "w") as file:
                file.write(json.dumps(data, indent=4))  
        # if there are no redemption questions,
        # then start picking questions from the bank
        else:
            # selects a question from each module with incrementing idx
            module_chosen = current_modules_selected[module_idx]
            
            # TODO: create list of tags selected by user
            # counts the number of times each tag was marked as correct
            tag_count_list = [
                tag["count"] for tag in data["bank"][module_chosen].values()
            ]
            # selects tags that are <= to the minimum number of the above list
            tags_to_be_chosen = [
                tag for tag, tag_count in data["bank"][module_chosen].items()
                if tag_count["count"] <= min(tag_count_list)
            ]
            # selects a random tag from the above list
            tag_chosen = random.choice(tags_to_be_chosen)
            
            # counts the number of times each question was marked as correct
            question_count_list = [
                question_count for question_count in data["bank"][module_chosen][tag_chosen]["questions"].values()
            ]
            # selects questions that are <= to the minimum number of the above list
            # and are not empty ("")
            questions_to_be_chosen = [
                question for question, question_count in data["bank"][module_chosen][tag_chosen]["questions"].items()
                if question_count <= min(question_count_list)
            ]
            # selects a random question from the above list
            question_chosen = random.choice(questions_to_be_chosen)
        
        question_location = [module_chosen, tag_chosen, question_chosen]
        
        # increment to the next module available
        module_idx += 1
        # if the module idx is the same as the size of the list,
        if module_idx == len(current_modules_selected):
            # then reset the module idx (prevents idx error)
            module_idx = 0
        
        # if there is no question that was preselected,
        # check for duplicate questions
        if "" in data["debug_question"]:
            is_duplicate_question = False
            for question in questions_to_be_chosen_final:
                # if the question is already in the final list,
                if question_location in question:
                    # then flag the question as a duplicate
                    is_duplicate_question = True
                    break
            for marked_wrong_question in data["questions_marked_wrong"]:
                # if the question was recently marked wrong,
                if question_location in marked_wrong_question:
                    # then flag the question as a duplicate
                    is_duplicate_question = True
                    break
            
            # if a duplicate question has been found,
            # then repeat the loop until a unique question has been selected
            if is_duplicate_question:
                continue
                
        result_chosen = question_bank[module_chosen][tag_chosen][question_chosen]
        details_chosen = result_chosen["details"]
        format_chosen = result_chosen["format"]
        
        # if the details are empty (meaning the questions need to be created)
        if details_chosen == None:
            # creates a random question and its associated answer
            question_chosen, correct_answer = result_chosen["variant"]()
        # if the details are not empty (meaning the questions are already typed)
        else:
            # selects a list of possible questions
            details_to_be_chosen = [
                key for key in details_chosen.keys()
                # if questions starts with rpt, do not add into the list
                # (only includes the first question)
                if not key.startswith("rpt")
            ]
            # chooses a random question from the list
            question_chosen = random.choice(details_to_be_chosen)
            # assigns with its associated answer
            correct_answer = details_chosen[question_chosen]
        
        # if there are different variants of the question and details are not empty
        # (meaning the question can be formed differently with other type of questions;
        # ex. What is the multiplier for _?)
        if result_chosen.get("variant") and details_chosen != None:
            # create a variant question
            question_chosen = Bank.get_variant_question(result_chosen["variant"],
                                                        question_chosen)
        
        # if the question format is multiple choice
        if format_chosen == MULTIPLE_CHOICE:
            # creates a list of incorrect choices to be chosen
            # excluding the correct answer
            choices_to_be_chosen = [
                choice for choice in details_chosen.values()
                if choice != correct_answer
            ]
            random.shuffle(choices_to_be_chosen)
            
            choices_chosen = []
            # adds 3 (incorrect) choices from the above randomized list
            for i in range(3):
                choices_chosen.append(choices_to_be_chosen[i])
            # then adds the correct answer as one of the choices
            choices_chosen.append(correct_answer)
            
            random.shuffle(choices_chosen)
        # if the question format is a select that apply
        elif format_chosen == SELECT_THAT_APPLY:
            # if the correct answer is already a list,
            # then question variant function was used
            if isinstance(correct_answer, list):
                variant_details = correct_answer
                
                # reassigns the single correct answer to multiple correct answers
                correct_answer = variant_details[0]
                # and choices to be chosen to multiple incorrect answers
                choices_to_be_chosen = variant_details[1]
            # otherwise, correct answer has not been reassigned
            # and there are no other variants to the question that exist
            else:
                correct_answer = details_chosen[question_chosen][0]
                choices_to_be_chosen = details_chosen[question_chosen][1]
                
            # combines the correct answer with the incorrect choices
            choices_chosen = correct_answer + choices_to_be_chosen
            random.shuffle(choices_chosen)
            
            # converts list into set (for exam grading purpose)
            correct_answer = set(correct_answer)
        # if the question format is a match to answer
        elif format_chosen == MATCH_TO_ANSWER or format_chosen == MATCH_TO_ANSWER_RANDOMIZED:
            subquestion_chosen_list = []
            correct_answer = [] # reassign the single correct answer to a list of correct answers
            choices_chosen = []
            
            # if there are more than 8 questions,
            if len(details_chosen[question_chosen]) > 8:
                # then set the maximum number of questions to 8
                maximum_number_of_match_to_answer = 8
            # otherwise,
            else:
                # set the maximum number of questions to the
                # number of available questions
                maximum_number_of_match_to_answer = len(details_chosen[question_chosen])
            
            # if subquestion ordering can be randomized
            if format_chosen == MATCH_TO_ANSWER_RANDOMIZED:
                random.shuffle(details_chosen[question_chosen])
            
            # iterate the amount of sub-questions/answer
            for i in range(maximum_number_of_match_to_answer):
                subquestion = details_chosen[question_chosen][i][0]
                answer = details_chosen[question_chosen][i][1]
                
                # adds the subquestion
                subquestion_chosen_list.append(subquestion)
                # adds the correct answer (in order)
                correct_answer.append(answer)
                # adds the choice (to later be shuffled)
                choices_chosen.append(answer)
                
            question_chosen = [question_chosen] + subquestion_chosen_list

            random.shuffle(choices_chosen)
        # if the question format is true or false
        elif format_chosen == TRUE_OR_FALSE:
            choices_chosen = ["True", "False"]
        # if the question format is free response
        elif format_chosen == FREE_RESPONSE:
            choices_chosen = None
        
        # adds the question to the list of questions to be chosen
        questions_to_be_chosen_final.append([
            question_location,
            
            question_chosen,
            correct_answer,
            format_chosen,
            choices_chosen,
        ])
        
    # shuffles the list
    random.shuffle(questions_to_be_chosen_final)
    
    return questions_to_be_chosen_final, maximum_number_of_questions

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

        # if the selected answer is a string
        if isinstance(selected_answer, str):
            # remove any white space
            selected_answer = selected_answer.strip()
            
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
    # if the question is "multiple choice", or "true or false"
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
    # if the question is a "select that apply"
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
            
            # if starts with a "-" (user wants to deselect their answer),
            if selected_answer.startswith("-"):
                # removes the answer
                selected_checkbox.remove(selected_answer[1:])
            # otherwise,
            else:
                # adds the answer
                selected_checkbox.add(selected_answer)
                
            on_update_selected_answer(selected_checkbox)
    # TODO: add break line between each question (probably have to extend window height)
    # if the question is a "match to answer" or "match to answer randomized"
    elif choice_format == MATCH_TO_ANSWER or choice_format == MATCH_TO_ANSWER_RANDOMIZED:
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
    # if the question is "free response"
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

# TODO: pack the widgets together for better readability
def display_current_question(action: str,
                             question_number_label: Label,
                             current_question_label: Label,
                             current_choice_frame: Frame,
                             current_answer_label: Label,
                             question_details_dict: dict,
                             maximum_number_of_questions: int,) -> None:
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
    if current_question_idx > maximum_number_of_questions:
        # loop back to the first question
        current_question_idx = 1
    # if attempting to navigate below the minimum questions
    elif current_question_idx < 1:
        # loop back to the last question
        current_question_idx = maximum_number_of_questions
    
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
    
    # if the question format is "match to answer" or "match to answer randomized",
    # then the value is a list
    if current_question["format"] == MATCH_TO_ANSWER or current_question["format"] == MATCH_TO_ANSWER_RANDOMIZED:
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
            
def on_enter_option(button: Button) -> None:
    """
    Changes the button texture
    when hovering over the button.
    """

    button.config(bg=HOVER_COLOR)

def on_leave_option(button: Button) -> None:
    """
    Changes the button texture
    when no longer hovering over the button.
    """

    button.config(bg=OPTION_COLOR)