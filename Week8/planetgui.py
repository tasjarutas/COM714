from tkinter import *
from tkinter import messagebox
from universe import Universe
from planet import Planet
from livingthinggui import LivingThingGui


class PlanetGui(Tk):
    def __init__(self):
        super().__init__()

        # Planet to populate
        self.planet = Planet()
        #self.livingthing = LivingThing()
        # set window attributes
        self.title("Planet GUI")

        # list of components
        self.name_label = Label()
        self.name_entry = Entry()
        self.name_submit_button = Button()
        #self.livingthing_label = Label()
        self.livingthing_button = Button()

        self.configure(bg="#768",
                       height=500,
                       width=500)
        self.add_name_label()
        self.add_name_entry()
        self.add_submit_button()
        #self.add_livingthing_label()
        self.add_livingthing_button()

    def add_name_label(self):
        # Add components to window
        self.name_label.grid(row=0, column=0)
        # Style the components
        self.name_label.configure(text="Enter Planet Name")

    def add_name_entry(self):
        # Add components to window
        self.name_entry.grid(row=0, column=1)
        # Style the components

    def add_submit_button(self):
        # Add components to window
        self.name_submit_button.grid(row=0, column=3)
        # Style the components
        self.name_submit_button.configure(text="Submit")

    def add_livingthing_label(self):
        # Add components to window
        self.livingthing_label.grid(row=1, column=0)
        # Style the components
        self.livingthing_label.configure(text="LivingThing")

    def add_livingthing_button(self):
        # Add components to window
        self.livingthing_button.grid(row=1, column=1)
        # Style the components
        self.livingthing_button.configure(text="Add LivingThing")
        # Assign events
        self.livingthing_button.bind("<ButtonRelease-1>", self.livingthing_button_clicked)

    def livingthing_button_clicked(self, event):
         self.destroy()
         self.add_livingthing_gui = LivingThingGui()
         self.add_livingthing_gui.mainloop()


if __name__ == '__main__':
    gui = PlanetGui()
    gui.mainloop()
