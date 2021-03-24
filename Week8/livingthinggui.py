from tkinter import *
from tkinter import messagebox
from universe import Universe
from livingthing import LivingThing
#from universegui import UniverseGui


class LivingThingGui(Tk):
    def __init__(self):
        super().__init__()

        # LivingThing to populate
        self.livingthing = LivingThing()
        # set window attributes
        self.title("LivingThing GUI")

        # list of components
        self.name_label = Label()
        self.name_entry = Entry()
        self.submit_button = Button()
        #self.home_button = Button()

        self.configure(bg="#768",
                       height=500,
                       width=500)
        self.add_name_label()
        self.add_name_entry()
        self.add_submit_button()
        #self.add_home_button()

    def add_name_label(self):
        # Add components to window
        self.name_label.grid(row=0, column=0)
        # Style the components
        self.name_label.configure(text="Enter Livingthing Name")

    def add_name_entry(self):
        # Add components to window
        self.name_entry.grid(row=1, column=0)
        # Style the components

    def add_submit_button(self):
        # Add components to window
        self.submit_button.grid(row=2, column=0)
        # Style the components
        self.submit_button.configure(text="Submit")
        # Assign events
        self.submit_button.bind("<ButtonRelease-1>", self.livingthing_button_clicked)

    def livingthing_button_clicked(self, event):
        messagebox.showinfo("Add LivingThing", "You have added living thing in a planet")

    def add_home_button(self):
        # Add components to window
        self.home_button.grid(row=2, column=1)
        # Style the components
        self.home_button.configure(text="Home")
        # Assign events
        self.home_button.bind("<ButtonRelease-1>", self.home_button_clicked)

    # def home_button_clicked(self, event):
    #     self.destroy()
    #     self.add_universegui = UniverseGui()
    #     self.add_universegui.mainloop()

if __name__ == '__main__':
    gui = LivingThingGui()
    gui.mainloop()
