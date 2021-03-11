from plant import Plant


class VenusFlytrap(Plant):

    def __init__(self, name: str, age: int = 0, energy: int = Plant.MAX_ENERGY) -> None:
        super().__init__(name, age, energy)

    def __repr__(self) -> str:
        return f'(name={self.__name}, age={self._age}, energy={self._energy})'

    def __str__(self) -> str:
        return f'{self._name} is {self._age} years old and has an energy of {self._energy}.'

    def catch(self, insects: int) -> None:
        potential_energy = self._energy + insects

        if potential_energy >= Plant.MAX_ENERGY:
            self._energy = Plant.MAX_ENERGY
            return potential_energy - Plant.MAX_ENERGY
        else:
            self._energy = potential_energy
            return self._energy - Plant.MAX_ENERGY
