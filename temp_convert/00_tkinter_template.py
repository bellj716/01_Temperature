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
                                              font=("Arial", "18", "bold"),
                                              bg=background_color,
                                              padx=10, pady=10)
            self.temp_converter_label.grid(row=0)

            #help button (row 1)
            self.help_button = Button(self.converter_frame, text="help",
                                      font=("Arial", "14"),
                                      padx=10, pady=-10, command=self.help)
            self.help_button.grid(row=1)

        def help(self):
            print("YOU HAVE REQUESTED HELP")
            get_help = Help(self)
            get_help.help_text.configure(text="HELP TEXT GOES HERE", font="Arial 8")

class Help:
    def __init__(self, partner):

        background = "orange"

        #disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        #if user press cross instead of dismiss, close help and release help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        #set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help and Instructions",
                                 font="Arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        #dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="orange", font="Arial 14 bold",
                                  command=partial(self.close_help,partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
