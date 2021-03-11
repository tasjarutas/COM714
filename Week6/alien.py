from livingthing import LivingThing
from flyingsuperpower import FlyingSuperPower
from invisibilitysuperpower import InvisibilitySuperPower


class Alien(LivingThing, FlyingSuperPower, InvisibilitySuperPower):
    def __init__(self, powers):
        self.super_powers = powers

    def fly(self, distance) -> None:
        if "fly" in self.super_powers:
            self.energy -= 10
        else:
            print("Do not have this power")
