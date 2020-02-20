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
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "18", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                                 text="Type in the amount to be "
                                                      "converted and then push "
                                                      "one of the buttons below",
                                                 font=("Arial", "14"), wrap=250, justify=LEFT,
                                                 bg=background_color, padx=10, pady=-10)
        self.temp_instructions_label.grid(row=1)

        # Temperature Entry Box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Celsius", font="Arial 12 bold",
                                  bg="khaki1", padx=10, pady=-10,
                                  command = lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 12 bold",
                                  bg="Orchid1", padx=10, pady=-10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer Label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color, pady=10,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 14 bold",
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 14 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, to):
        print(to)

        # retrieve amount entered into entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            print("A")

        except ValueError:
            print("B")

        # check amount is a valid number

        # convert to f

        # convert to c

        # round!!

        # display answer

        # add answer to list for history


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertwe")
    root.resizable(width=False, height=False)
    something = Converter(root)
    root.mainloop()
