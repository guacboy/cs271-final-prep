from tkinter import *

BG_COLOR = "#2b2b2c"
DETAILS_BG_COLOR = "#1e1e1e"
OPTION_COLOR = "#404040"
HOVER_COLOR = "#7c7c7c"
FONT_COLOR = "#f5f5f5"

FONT = "Helvetica"

class Util():
    """
    Creates widgets.
    """
    
    def frame(window) -> Frame:
        return Frame(window,
                     bg=BG_COLOR,)
    
    def button(window) -> Button:
        return Button(window,
                      font=(FONT, 15, "bold"),
                      fg=FONT_COLOR,
                      bg=OPTION_COLOR,
                      activeforeground=FONT_COLOR,
                      activebackground=OPTION_COLOR,
                      padx=30,
                      pady=15,)
        
    def label(window) -> Label:
        return Label(window,
                     font=(FONT, 15, "bold"),
                     fg=FONT_COLOR,
                     bg=BG_COLOR,)
        
    def radiobutton(window) -> Radiobutton:
        return Radiobutton(window,
                           font=(FONT, 15, "normal"),
                           fg=FONT_COLOR,
                           bg=BG_COLOR,
                           activeforeground=FONT_COLOR,
                           activebackground=BG_COLOR,
                           selectcolor=OPTION_COLOR,
                           justify=LEFT,
                           wraplength=250,
                           tristatevalue="None",)
        
    def entry(window) -> Entry:
        return Entry(window,
                     font=(FONT, 15, "normal"),
                     width=20,
                     fg=FONT_COLOR,
                     bg=OPTION_COLOR,
                     relief=RAISED,
                     bd=2,)
        
    def checkbox(window) -> Checkbutton:
        return Checkbutton(window,
                           font=(FONT, 15, "normal"),
                           fg=FONT_COLOR,
                           bg=BG_COLOR,
                           activeforeground=FONT_COLOR,
                           activebackground=BG_COLOR,
                           selectcolor=OPTION_COLOR,
                           justify=LEFT,
                           wraplength=750,
                           padx=5,)
        
    def optionmenu(window,
                   option,
                   *choices,
                   func=None,) -> OptionMenu:
        optionmenu = OptionMenu(window,
                                option,
                                *choices,
                                command=func,)
        optionmenu.config(font=(FONT, 15, "normal"),
                          fg=FONT_COLOR,
                          bg=OPTION_COLOR,
                          activeforeground=FONT_COLOR,
                          activebackground=HOVER_COLOR,
                          highlightbackground=BG_COLOR,
                          width=10,)
        return optionmenu