from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Tickets")
        self.configure(bg="#768",
                   height=500,
                   width=500)

        self.add_heading_label()
        self.add_instruction_label()
        #self.add_tickets_entry()
        self.add_buy_button()

    def add_heading_label(self):
        #Create the component
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)

        #Style the component
        self.heading_label.configure(font="Arial 24",
                                 text="This is a heading.")

        #Add event handlers to the component

    def add_instruction_label(self):
        #Create the component
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0)

    def add_tickets_entry(self):
        pass

    def add_buy_button(self):
         # create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)

        # style
        self.buy_button.configure(text="Submit")

        # events
        self.buy_button.bind("<ButtonRelease-1>", self.buy_button_clicked)

    def buy_button_clicked(self, event):
        messagebox.showinfo("Purchased!", "You have purchased the tickets!")


if __name__ == '__main__':
    gui = Gui()
    gui.mainloop()
