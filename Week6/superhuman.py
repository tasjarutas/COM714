from animal import Animal
from human import Human
from flyingsuperpower import FlyingSuperPower


class SuperHuman(Human, FlyingSuperPower):

    FLY_ENERGY = 5

    def __init__(self, name: str, age: int = 0, energy: int = Animal.MAX_ENERGY) -> None:
        super().__init__(name, age, energy)
        self.__clothing = []

    def __repr__(self) -> str:
        return f'SuperHuman (name={self._name}, age={self._age}, energy={self._energy})'

    def __str__(self) -> str:
        return f'{self._name} is {self._age} years old and has an energy of {self._energy}.'

    def fly(self, distance) -> None:
        potential_energy = self._energy - distance
        if potential_energy >= self.FLY_ENERGY:
            print("I'm flying")
            return True
        else:
            print("Not enough energy to fly")
            return False



