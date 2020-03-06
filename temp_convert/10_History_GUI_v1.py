from tkinter import *
from functools import partial # To prevent unwanted windows

import random

if __name__ == '__main__':
    class Converter:
        def __init__(self, parent):

            # Formatting variables...
            background_color = "light blue"

            # in actual program this is blank and is populated with calculations.
            self.all_calculations = ['10 degrees F is -12.2 degrees C',
                                     '13 degrees F is -10.6 degrees C',
                                     '250 degrees F is 121.1 degrees C',
                                     '-100 degrees F is -73.3 degrees C',
                                     '785 degrees F is 418.3 degrees C',
                                     '45 degrees F is 7.2 degrees C',
                                     '70 degrees F is 21.1 degrees C']

            # Converter Main Screen GUI
            self.converter_frame = Frame(width=500, height=700, bg=background_color, pady=10)
            self.converter_frame.grid()

            # Temperature converion heading row 0
            self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                              font=("Arial", "18", "bold"),
                                              bg=background_color,
                                              padx=10, pady=10)
            self.temp_converter_label.grid(row=0)

            #history button (row 1)
            self.history_button = Button(self.converter_frame, text="History",
                                      font=("Arial", "14"),
                                      padx=10, pady=-10, command=self.history)
            self.history_button.grid(row=1)

        def history(self):
            print("YOU HAVE REQUESTED History")
            get_history = history(self)
            get_history.history_text.configure(text="History TEXT GOES HERE", font="Arial 8")

class history:
    def __init__(self, partner):

        background = "orange"

        #disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        #if user press cross instead of dismiss, close history and release history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # set up gui frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        #set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="Arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                                           "calculations. Please use the "
                                                           "export buttone and create a text"
                                                           "file of all your calculations"
                                                           "for this session", font="Arial 12 italic",
                                                            justify=LEFT, width=40, bg=background,
                                                            wrap=250, fg="maroon", padx=10, pady=-10)
        self.history_text.grid(row=1)

        # History Output (row 2)

        # dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 14 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                     font="Arial 14 bold")
        self.export_button.grid(row=0, column=0)

    def close_history(self, partner):
        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
