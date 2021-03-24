class LivingThing:
    REPRODUCE_ENERGY = 1
    MAX_ENERGY = 100
    MIN_ENERGY = 0
    MOVE_ENERGY = 10

    def __init__(self, name: str='', age: int = 0, energy: int = 100) -> None:
        self._name = name
        self._age = age
        self._energy = energy

    def __repr__(self) -> str:
        return f'Living_thing (name={self._name}, age={self._age}, energy={self._energy})'

    def __str__(self) -> str:
        return f'{self._name} is {self._age} years old'

    def grow(self) -> None:
        self._age += 1

    def reproduce(self) -> bool:
        potential_energy = self._energy - LivingThing.REPRODUCE_ENERGY

        if potential_energy >= LivingThing.REPRODUCE_ENERGY:
            self._energy = potential_energy
            return True
        else:
            return False
