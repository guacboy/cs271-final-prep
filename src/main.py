from tkinter import *
import json

from util import *
from bank import question_bank
from exam import create_exam

root = Tk()
root.geometry("1500x800")
root.config(background=BG_COLOR)

def main_menu() -> None:
    """
    Displays main menu GUI.
    """
    
    with open("data.json", "r") as file:
            data = json.load(file)
    
    subject_frame = Util.frame(root)
    subject_frame.pack(side=TOP,
                       pady=(10,0))
    
    column_group = [
        ["Module 1"],
        ["Module 2", "Module 3", "Module 4"],
        ["Module 5", "Module 6", "Module 7"],
        ["Module 8", "Module 9"]
    ]
    
    module_checkbox_dict = {}
    # iterates through all the modules
    # FIXME: modules not aligning correctly
    for group in column_group:
        # creates a frame to organize the modules' columns
        # (for more compact viewing)
        column_frame = Util.frame(subject_frame)
        column_frame.pack(side=LEFT,
                          anchor=N,)
        
        for module in group:
            # creates a frame to organize the modules with their tags
            subject_inner_frame = Util.frame(column_frame)
            subject_inner_frame.pack()
            
            option = StringVar(value=f"-{module}")
            # creates the module checkbox
            module_checkbox = Util.checkbox(subject_inner_frame)
            module_checkbox.config(text=module,
                                   onvalue=module,
                                   offvalue=f"-{module}",
                                   variable=option,
                                   command=lambda o=option, cb=module_checkbox: on_update_module_selected(o.get(), cb))
            module_checkbox.pack(side=TOP,
                                 anchor=W,)
            
            # creates a list of all the tag checkboxes under *this* module
            module_checkbox_dict.update({
                module: {
                    module_checkbox: []
                }
            })
            
            # iterates through all the tags
            for tag in question_bank[module].keys():
                tag_frame = Util.frame(subject_inner_frame)
                tag_frame.pack(side=TOP,
                               anchor=W,)
                
                # creates a padding to the left
                left_padding = Util.label(tag_frame)
                left_padding.config(text=" ")
                left_padding.pack(side=LEFT)
                
                option = StringVar(value=f"-{tag}")
                # creates the tag checkbox
                tag_checkbox = Util.checkbox(tag_frame)
                tag_checkbox.config(text=tag,
                                    font=(FONT, 10, "normal"),
                                    onvalue=tag,
                                    offvalue=f"-{tag}",
                                    variable=option,
                                    command=lambda o=option: on_update_tag_selected(o.get()))
                tag_checkbox.pack(side=LEFT)
                
                # if any checkboxes were previously selected (from a different instance),
                if tag in data["questions_selected"][module]:
                    # then select those checkboxes
                    module_checkbox.select()
                    tag_checkbox.select()
                
                # adds the tag checkbox into a list under their module
                module_checkbox_dict[module][module_checkbox].append({tag: tag_checkbox})
                
                # creates the number of questions within that tag
                question_count_label = Util.label(tag_frame)
                question_count_label.config(text=f"{len(question_bank[module][tag])} Qs",
                                            font=(FONT, 8, "bold"))
                question_count_label.pack(side=LEFT)
    
    def on_update_module_selected(module_selected: str,
                                  module_checkbox: Checkbutton) -> None:
        """
        Updates the data.json file with the modules selected.
        """

        with open("data.json", "r") as file:
            data = json.load(file)
        
        # if starts with a "-" (user wants to deselect their module),
        if module_selected.startswith("-"):
            # deselects their checkboxes
            for tag_list in module_checkbox_dict[module_selected[1:]][module_checkbox]:
                for tag_checkbox in tag_list.values():
                    tag_checkbox.deselect()
                # and removes the tags
                data["questions_selected"][module_selected[1:]].clear()
        # otherwise,
        else:
            # adds the tags and selects their checkboxes
            for tag_list in module_checkbox_dict[module_selected][module_checkbox]:
                for tag, tag_checkbox in tag_list.items():
                    # if the tag has not already been added into the list
                    if tag not in data["questions_selected"][module_selected]:
                        data["questions_selected"][module_selected].append(tag)
                    tag_checkbox.select()
        
        with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))
    
    def on_update_tag_selected(tag_selected: str) -> None:
        """
        Updates the data.json file with the tags selected.
        """
        
        with open("data.json", "r") as file:
            data = json.load(file)
        
        module_selected = None
        # iterates through the entire question bank to find
        # which module the tag belongs in
        for module in question_bank:
            for tag in question_bank[module].keys():
                # if the module location is found
                if tag_selected == tag or tag_selected[1:] == tag:
                    # mark the module
                    module_selected = module
                    break
            # if the module has been marked,
            if module_selected != None:
                # then break out of the entire loop
                break
        
        # if starts with a "-" (user wants to deselect their tag),
        if tag_selected.startswith("-"):
            # removes the tag
            data["questions_selected"][module_selected].remove(tag_selected[1:])
        # otherwise,
        else:
            # adds the tag
            data["questions_selected"][module_selected].append(tag_selected)
        
        with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))
        
        # if there is at least one tag for the module selected,
        if len(data["questions_selected"][module_selected]) > 0:
            # then select the module's checkbox
            for module_checkbox in module_checkbox_dict[module_selected]:
                module_checkbox.select()
        # if there are no tags selected for the module selected,
        elif len(data["questions_selected"][module_selected]) == 0:
            # then deselect the module's checkbox
            for module_checkbox in module_checkbox_dict[module_selected]:
                module_checkbox.deselect()
    
    # erases the data in data.json
    erase_data_label = Util.label(root)
    erase_data_label.config(text="ERASE DATA",
                            font=(FONT, 10, "bold"),)
    erase_data_label.bind("<Enter>", func=lambda e: on_enter_erase_data())
    erase_data_label.bind("<Leave>", func=lambda e: on_leave_erase_data())
    erase_data_label.bind("<Button-1>", func=lambda e: on_click_erase_data())
    erase_data_label.pack(side=BOTTOM,
                          pady=(10, 25))
    
    def on_enter_erase_data() -> None:
        """
        Changes the button texture
        when hovering over the button.
        """
        
        # if the data has recently (within 3 seconds) been reset
        if erase_data_label.cget("text") != "POOF!":
            erase_data_label.config(text="ERASE DATA",
                                    font=(FONT, 10, "bold underline"),
                                    fg="#cd4545",)
        
    def on_leave_erase_data() -> None:
        """
        Changes the button texture
        when no longer hovering over the button.
        """
        
        erase_data_label.config(font=(FONT, 10, "bold"),
                                fg=FONT_COLOR,)
        
    def on_click_erase_data() -> None:
        """
        Erases any data and reloads the data.json file.
        """
        
        with open("data.json", "r") as file:
            data = json.load(file)
        
        data["bank"].clear()
        data["redemption_questions"].clear()
        data["questions_marked_wrong"].clear()
        
        with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))
        
        erase_data_label.config(text="POOF!",
                                font=(FONT, 10, "bold"),
                                fg=FONT_COLOR,)
        erase_data_label.unbind("<Button-1>")
        
        def reset_erase_data_button() -> None:
            """
            Reverts back to original state.
            """
            
            erase_data_label.config(text="ERASE DATA")
            erase_data_label.bind("<Button-1>", func=lambda e: on_click_erase_data())
        
        root.after(3000, reset_erase_data_button)
        create_json() # creates/updates the json file
    
    # TODO: disable button if questions selected list is empty, or if exam window is opened
    
    # creates the exam
    create_button = Util.button(root)
    create_button.config(text="Create Exam",
                         command=lambda: [
                             create_exam(root),
                             root.iconify(),
                         ])
    create_button.bind("<Enter>", func=lambda e: on_enter_option(create_button))
    create_button.bind("<Leave>", func=lambda e: on_leave_option(create_button))
    create_button.pack(side=BOTTOM)
    
    with open("data.json", "r") as file:
        data = json.load(file)
    
    # if a question has not been selected,
    if "" in data["debug_question"]:
        # then make the clear debugger button visible
        clear_debugger_fg = BG_COLOR
        
        # ensures any previous (incomplete) selections are removed
        data["debug_question"] = [""] * 3
        
        with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))
    # otherwise,
    else:
        # make the clear debugger button invisible
        clear_debugger_fg = FONT_COLOR
    
    # clears the debugger tool
    clear_debugger_label = Util.label(root)
    clear_debugger_label.config(text="CLEAR",
                                font=(FONT, 10, "bold"),
                                fg=clear_debugger_fg,) # makes the 'clear debugger' button invisible
    clear_debugger_label.bind("<Enter>", func=lambda e: on_enter_clear_debugger())
    clear_debugger_label.bind("<Leave>", func=lambda e: on_leave_clear_debugger())
    clear_debugger_label.bind("<Button-1>", func=lambda e: on_click_clear_debugger())
    clear_debugger_label.pack(side=BOTTOM,
                              pady=(0,10))
    
    def on_enter_clear_debugger() -> None:
        """
        Changes the button texture
        when hovering over the button.
        """
        
        # if the button is currently not invisible
        if clear_debugger_label.cget("fg") != BG_COLOR:
            clear_debugger_label.config(font=(FONT, 10, "bold underline"),
                                        fg="#cd4545",)
        
    def on_leave_clear_debugger() -> None:
        """
        Changes the button texture
        when no longer hovering over the button.
        """
        # if the button is currently not invisible
        if clear_debugger_label.cget("fg") != BG_COLOR:
            clear_debugger_label.config(font=(FONT, 10, "bold"),
                                        fg=FONT_COLOR,)
     
    def on_click_clear_debugger() -> None:
        """
        Clears the debugger selections.
        """
        
        with open("data.json", "r") as file:
            data = json.load(file)
        
        data["debug_question"] = [""] * 3
        
        with open("data.json", "w") as file:
            file.write(json.dumps(data, indent=4))
        
        # iterates through the widgets in the debug frame
        for optionmenu in debug_frame.winfo_children():
            # if it's an optionmenu,
            if isinstance(optionmenu, OptionMenu):
                # then reset the optionmenu
                optionmenu.destroy()
        
        on_create_debug_optionmenu()
        
        # makes the 'clear debugger' button invisible
        clear_debugger_label.config(fg=BG_COLOR)
    
    # creates a debugger tool to view specific questions
    debug_frame = Util.frame(root)
    debug_frame.pack(side=BOTTOM,
                     pady=(0,0))
    debug_label = Util.label(debug_frame)
    debug_label.config(text="DEBUG TOOL",
                       font=(FONT, 10, "bold"),)
    debug_label.pack(side=TOP)
    
    def on_create_debug_optionmenu() -> None:
        """
        Creates the debugger options.
        """
        
        with open("data.json", "r") as file:
            data = json.load(file)
        
        module = data["debug_question"][0]
        tag = data["debug_question"][1]
        question = data["debug_question"][2]
        
        # if there is a debug question (checks if the last idx is empty),
        if "" in data["debug_question"]:
            # creates placeholder variables
            tag_choices = [""]
            question_choices = [""]
            # and disables the optionmenu
            current_state = DISABLED
        # otherwise,
        else:
            # select the current choices available
            tag_choices = [
                tag for tag in question_bank[module].keys()
            ]
            question_choices = [
                question for question in question_bank[module][tag].keys()
            ]
            # and enables the optionmenu
            current_state = ACTIVE
        
        module_option = StringVar(value=module)
        # selects the current modules available
        module_choices = [
            module for module in question_bank.keys()
        ]
        # creates the module optionmenu
        debug_module_optionmenu = Util.optionmenu(debug_frame,
                                                  module_option,
                                                  *module_choices,
                                                  func=lambda e: on_update_debug_optionmenu(e),)
        debug_module_optionmenu.pack(side=LEFT)
        
        tag_option = StringVar(value=tag)
        # creates the tag optionmenu
        debug_tag_optionmenu = Util.optionmenu(debug_frame,
                                               tag_option,
                                               *tag_choices,
                                               func=lambda e: on_update_debug_optionmenu(module,
                                                                                         e),)
        debug_tag_optionmenu.config(width=30,
                                    state=current_state,)
        debug_tag_optionmenu.pack(side=LEFT)
        
        question_option = StringVar(value=question)
        # creates the question optionmenu
        debug_question_optionmenu = Util.optionmenu(debug_frame,
                                                    question_option,
                                                    *question_choices,
                                                    func=lambda e: on_update_debug_optionmenu(module,
                                                                                              tag,
                                                                                              e,),)
        debug_question_optionmenu.config(state=current_state)
        debug_question_optionmenu.pack(side=LEFT)
        
    on_create_debug_optionmenu()
    
    def on_update_debug_optionmenu(module: str="",
                                   tag: str="",
                                   question: str="",):
        """
        Updates both the tag's optionmenu and question's optionmenu
        with new settings.
        """
        
        # create the list of optionmenus
        debug_optionmenu = [
            debug for debug in debug_frame.winfo_children()
            if isinstance(debug, OptionMenu)
        ]
        
        # for every option except the first option
        # (the module option)
        for debug in debug_optionmenu[1::]:
            # delete the widget (to later be recreated with new choices)
            debug.destroy()
        
        tag_option = StringVar(value=tag)
        # selects the current tags available
        tag_choices = [
            tag for tag in question_bank[module].keys()
        ]
        debug_tag_optionmenu = Util.optionmenu(debug_frame,
                                               tag_option,
                                               *tag_choices,
                                               func=lambda e: on_update_debug_optionmenu(module,
                                                                                         e),)
        debug_tag_optionmenu.config(width=30,)
        debug_tag_optionmenu.pack(side=LEFT)
        
        question_option = StringVar(value=question)
        
        # if a tag has not been selected
        if tag == "":
            # creates a placehold variable
            question_choices = [""]
            # and disables the optionmenu
            current_state = DISABLED
        # if a tag has been selected
        else:
            # selects the current questions available
            question_choices = [
                question for question in question_bank[module][tag].keys()
            ]
            # and enables the optionmenu
            current_state = ACTIVE
        
        debug_question_optionmenu = Util.optionmenu(debug_frame,
                                                    question_option,
                                                    *question_choices,
                                                    func=lambda e: on_update_debug_optionmenu(module,
                                                                                              tag,
                                                                                              e),)
        debug_question_optionmenu.config(state=current_state)
        debug_question_optionmenu.pack(side=LEFT)
        
        # makes the 'clear debugger' button visible
        clear_debugger_label.config(fg=FONT_COLOR)
        
        def on_update_question_location(module: str,
                                        tag: str,
                                        question: str) -> None:
            """
            Updates the debug question to its preselected values.
            """
            
            with open("data.json", "r") as file:
                data = json.load(file)
            
            data["debug_question"] = [module, tag, question]
            
            with open("data.json", "w") as file:
                file.write(json.dumps(data, indent=4))
                
        on_update_question_location(module, tag, question)
    
def create_json() -> None:
    """
    Populates the JSON file, updating any new changes.
    """
    
    with open("data.json", "r") as file:
        data = json.load(file)
    
    for module in question_bank:
        # if the module has not been added
        if module not in data["bank"]:
            # adds the module as one of the available options
            data["bank"].update({
                module: {},
            })
        # if the module has not been added
        if module not in data["questions_selected"]:
            # adds the module as one of the current selections
            data["questions_selected"].update({
                module: [],
            })
        for tag in question_bank[module]:
            # if the tag has not been added
            if tag not in data["bank"][module]:
                # # adds the tag as one of the available options
                data["bank"][module].update({
                    tag: {
                        "questions": {},
                        "count": 0,
                    }
                })
            for question in question_bank[module][tag]:
                # if the question has not been added
                if question not in data["bank"][module][tag]["questions"]:
                    # # adds the question as one of the available options
                    data["bank"][module][tag]["questions"].update({
                        question: 0,
                    })
        
    with open("data.json", "w") as file:
        file.write(json.dumps(data, indent=4))

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

if __name__ == "__main__":
    create_json() # creates/updates the json file
    main_menu()
    root.mainloop()
    