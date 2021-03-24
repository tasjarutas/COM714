from tkinter import *
from tkinter import messagebox
from universe import Universe
from non_planet import NonPlanet


class NonPlanetGui(Tk):
    def __init__(self):
        super().__init__()

        # universe to poplulate
        self.non_planet = NonPlanet()
        # set window attributes
        self.title("NonPlanet GUI")

        # list of components
        self.name_label = Label()
        self.name_entry = Entry()
        self.submit_button = Button()

        self.configure(bg="#768",
                       height=500,
                       width=500)
        self.add_name_label()
        self.add_name_entry()
        self.add_submit_button()

    def add_name_label(self):
        # Add components to window
        self.name_label.grid(row=0, column=0)
        # Style the components
        self.name_label.configure(text="Enter Planet Name")

    def add_name_entry(self):
        # Add components to window
        self.name_entry.grid(row=1, column=0)
        # Style the components

    def add_submit_button(self):
        # Add components to window
        self.submit_button.grid(row=2, column=0)
        # Style the components
        self.submit_button.configure(text="Submit")


if __name__ == '__main__':
    gui = NonPlanetGui()
    gui.mainloop()
