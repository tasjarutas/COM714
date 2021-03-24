from plant import Plant
from invisibilitysuperpower import InvisibilitySuperPower


class SuperPlant(Plant,InvisibilitySuperPower):
    MIN_INVISIBLE_ENERGY = 3

    def __init__(self, name: str, age: int = 0, energy: int = Plant.MAX_ENERGY) -> None:
        super().__init__(name, age, energy)

    def __repr__(self) -> str:
        return f'SuperPlant (name={self._name}, age={self._age}, energy={self._energy})'

    def __str__(self) -> str:
        return f'{self._name} is {self._age} years old and has an energy of {self._energy}.'

    def turn_visible(self) -> None:
        print("I am visible")
        return True

    def turn_invisible(self) -> None:

        if self._energy >= SuperPlant.MIN_INVISIBLE_ENERGY:
            print("I am now invisible")
            return True
        else:
            print("Not enough energy to turn invisible")
            return False
