from tkinter import *
from tkinter import messagebox
from universe import Universe
from planetgui import PlanetGui

class UniverseGui(Tk):
    def __init__(self):
        super().__init__()

        #universe to poplulate
        self.universe = Universe()
        # set window attributes
        self.title("Universe GUI")

        #list of components
        self.planets_label = Label()
        self.planets_list = Listbox()
        self.planet_button = Button()

        self.configure(bg="#768",
                   height=500,
                   width=500)
        self.add_planets_label()
        self.add_planets_list()
        self.add_planet_button()

    def add_planets_label(self):
        #Add components to window
        self.planets_label.grid(row=0,column=0)
        #Style the components
        self.planets_label.configure(text="Existing Planets")

    def add_planets_list(self):
         #Add components to window
        self.planets_list.grid(row=1,column=0)
        #Style the components


    def add_planet_button(self):
         #Add components to window
        self.planet_button.grid(row=2,column=0)
        #Style the components
        self.planet_button.configure(text="Add Planet")
        #Assign events
        self.planet_button.bind("<ButtonRelease-1>",self.planet_button_clicked)

    def planet_button_clicked(self, event):
        self.destroy()
        self.add_planet_gui = PlanetGui()
        self.add_planet_gui.mainloop()

if __name__ == '__main__':
    gui = UniverseGui()
    gui.mainloop()
