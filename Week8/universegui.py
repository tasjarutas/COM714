from tkinter import *
from tkinter import messagebox
from universe import Universe
from planetgui import PlanetGui
from nonplanetgui import NonPlanetGui


class UniverseGui(Tk):
    def __init__(self):
        super().__init__()

        # universe to populate
        self.universe = Universe()
        # set window attributes
        self.title("Universe GUI")

        # list of components
        self.planets_label = Label()
        self.planets_list = Listbox()
        self.planet_button = Button()

        self.non_planets_label = Label()
        self.non_planets_list = Listbox()
        self.non_planet_button = Button()

        self.configure(bg="#768",
                       height=500,
                       width=500)
        self.add_top_label()
        self.add_list()
        self.add_button()

    def add_top_label(self):
        # Add components to window
        self.planets_label.grid(row=0, column=0)
        self.non_planets_label.grid(row=0, column=1)
        # Style the components
        self.planets_label.configure(text="Existing Planets")
        self.non_planets_label.configure(text="Existing NonPlanets")

    def add_list(self):
        # Add components to window
        self.planets_list.grid(row=1, column=0)
        self.non_planets_list.grid(row=1, column=1)

    def add_button(self):
        # Add components to window
        self.planet_button.grid(row=2, column=0)
        self.non_planet_button.grid(row=2, column=1)

        # Style the components
        self.planet_button.configure(text="Add Planet")
        self.non_planet_button.configure(text="Add NonPlanet")

        # Assign events
        self.planet_button.bind("<ButtonRelease-1>", self.planet_button_clicked)
        self.non_planet_button.bind("<ButtonRelease-1>", self.non_planet_button_clicked)

    def planet_button_clicked(self, event):
         self.destroy()
         self.add_planet_gui = PlanetGui()
         self.add_planet_gui.mainloop()

    def non_planet_button_clicked(self, event):
         self.destroy()
         self.add_non_planet_gui = NonPlanetGui()
         self.add_non_planet_gui.mainloop()


if __name__ == '__main__':
    gui = UniverseGui()
    gui.mainloop()
