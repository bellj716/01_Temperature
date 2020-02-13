from tkinter import *
from functools import partial       # to prevent unwanted windows
import random


class Converter:
    def __init__(self, parent):

        # formatting variables
        background_color = "light blue"

        # Converter Frame
        self.converter_frame = Frame(width=500, height=700, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "18", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User instructions (row 1)
            self.help_button = Button(self.converter_frame, text="help",
                                      font=("Arial", "14"),
                                      padx=10, pady=-10, command=self.help)
            self.help_button.grid(row=1)

        def help(self):
            print("YOU HAVE REQUESTED HELP")
            get_help = Help(self)
            get_help.help_text.configure(text="HELP TEXT GOES HERE", font="Arial 8")

        # Temperature Entry Box (row 2)

        # Conversion buttons frame (row 3)

        # Answer Label (row 4)

        # History / Help button frame (row 5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Foo(root)
    root.mainloop()
