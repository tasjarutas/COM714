from plant import Plant
from invisibilitysuperpower import InvisibilitySuperPower


class SuperPlant(Plant,InvisibilitySuperPower):
    INVISIBLE_ENERGY = 3

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
        potential_energy = self._energy - self.INVISIBLE_ENERGY
        if potential_energy >= self.INVISIBLE_ENERGY:
            print("I am now invisible")
            return True
        else:
            return False