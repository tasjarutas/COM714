from dog import Dog
from flyingsuperpower import FlyingSuperPower
from speedsuperpower import SpeedSuperPower


class SuperDog(Dog, FlyingSuperPower, SpeedSuperPower):

    def __init__(self, powers):
        self.super_powers = powers

    # override method bark of class Dog
    def bark(self) -> None:
        print("Super!")
        super().bark()

    def fly(self, distance) -> None:
        if "fly" in self.super_powers:
            self.energy -= 10
        else:
            print("Do not have this power")

    def run_fast(self, distance) -> None:  #
        if "speed" in self.super_powers:
            self.energy -= 15
        else:
            print("Do not have this power")
