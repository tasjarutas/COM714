from livingthing import LivingThing
from flyingsuperpower import FlyingSuperPower
from invisibilitysuperpower import InvisibilitySuperPower
from super_power import SuperPower


class Alien(LivingThing, FlyingSuperPower, InvisibilitySuperPower):
    def __init__(self, name, powers):
        super(LivingThing, self).__init__(name)
        self.super_powers = powers

    def fly(self, distance) -> None:
        if SuperPower.FLYING in self.super_powers:
            print("I'm flying as Alien")
        else:
            print("Alien can not fly yet")

    def turn_visible(self) -> None:
        print("I am visible as Alien")

    def turn_invisible(self) -> None:
        if SuperPower.INVISIBILITY in self.super_powers:
            print("I turn to be invisible as Alien")
        else:
            print("Alien can not turn invisible yet")

