from tkinter import *
from functools import partial       # to prevent unwanted windows
import random

class Converter:
    def __init__(self, parent):

        # formatting variables
        background_color = "light blue"

        # in actual program this is blank and is populated with calculations.
        self.all_calculations = ['10 degrees F is -12.2 degrees C',
                                 '13 degrees F is -10.6 degrees C',
                                 '250 degrees F is 121.1 degrees C',
                                 '-100 degrees F is -73.3 degrees C',
                                 '785 degrees F is 418.3 degrees C',
                                 '45 degrees F is 7.2 degrees C',
                                 '70 degrees F is 21.1 degrees C']

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

        # History / history button frame (row 5)
        self.hist_history_frame = Frame(self.converter_frame)
        self.hist_history_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_history_frame, font="Arial 14 bold",
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.history_button = Button(self.hist_history_frame, font="Arial 14 bold",
                                  text="History", width=5)
        self.history_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"       # Pale pink background for when entry has errors

        # retrieve amount entered into entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # check amount is a valid number

            # convert to f
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # convert to c
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                #input is invalid (too cold)
                answer = "Too Cold!"
                has_errors = "yes"

            #display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")

            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    root.resizable(width=False, height=False)
    something = Converter(root)
    root.mainloop()
