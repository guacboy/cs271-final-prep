from tkinter import *

BG_COLOR = "#2b2b2c"
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