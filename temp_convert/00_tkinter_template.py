from tkinter import *
from functools import partial # To prevent unwanted windows

import random

if __name__ == '__main__':
    class Converter:
        def __init__(self, parent):

            # Formatting variables...
            background_color = "light blue"

            # Converter Main Screen GUI
            self.converter_frame = Frame(width=500, height=700, bg=background_color, pady=10)
            self.converter_frame.grid()

            # Temperature converion heading row 0
            self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                              font=("Papyrus", "18", "bold"),
                                              bg=background_color,
                                              padx=10, pady=10)
            self.temp_converter_label.grid(row=0)

            #help button (row 1)
            self.help_button = Button(self.converter_frame, text="help",
                                      font=("Papyrus", "12"),
                                      padx=10, pady=-10)
            self.help_button.grid(row=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
