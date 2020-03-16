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

            #export button (row 1)
            self.export_button = Button(self.converter_frame, text="export",
                                      font=("Arial", "14"),
                                      padx=10, pady=-10, command=self.export)
            self.export_button.grid(row=1)

        def export(self):
            get_export = Export(self)


class Export:
    def __init__(self, partner):

        background = "orange"

        #disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        #if user press cross instead of dismiss, close export and release export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # set up gui frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        #set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export and Instructions",
                                 font="Arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text=" Enter a filename in the box below "
                                 "and press the save button to save your "
                                 "Calculation history to a text file."
                                 "if the filename you enter below already exists, "
                                 "its contents will be replaced with your calculation "
                                 "History",
                                 justify=LEFT, width=40, bg=background,
                                 wrap=250)
        self.export_text.grid(row=1)

        #Warning Text (Label, row 2)
        self.export_text = Button(self.export_frame,
                                  text="Save", width=10,
                                  bg="orange", font="Arial 14 bold",
                                  command=partial(self.close_export,partner))
        self.export_text.grid(row=2, pady=10)

        # Save / Cancel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Cancel",
                                  command=partial(self.close_export, partner))
        self.save_button.grid(row=0, column=1)

    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
