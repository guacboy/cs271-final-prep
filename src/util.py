from tkinter import *

BG_COLOR = "#2b2b2c"
OPTION_COLOR = "#404040"
FONT_COLOR = "#f5f5f5"

class Util():
    """
    Creates widgets.
    """
    
    def frame(window) -> Frame:
        return Frame(window,
                     bg=BG_COLOR,)
    
    def button(window) -> Button:
        return Button(window,
                      font=("Helvetica", 15, "bold"),
                      fg=FONT_COLOR,
                      bg=OPTION_COLOR,
                      padx=30,
                      pady=15,)
        
    def label(window) -> Label:
        return Label(window,
                     font=("Helvetica", 15, "bold"),
                     fg=FONT_COLOR,
                     bg=BG_COLOR,)