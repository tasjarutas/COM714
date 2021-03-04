from livingthing import LivingThing


class Animal(LivingThing):
    MAX_ENERGY = 100
    MIN_ENERGY = 0
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name: str, age: int = 0, energy: int = LivingThing.MAX_ENERGY) -> None:
        # self.__name = name
        # self.__age = age
        # self.__energy = energy
        super().__init__(name, age, energy)

    def __repr__(self) -> str:
        return f'Animal(name={self._name}, age={self._age}, energy={self._energy})'

    def __str__(self) -> str:
        return f'{self._name} is {self._age} years old and has an energy of {self._energy}.'

    def move(self, distance: int) -> bool:
        potential_energy = self._energy - distance

        if potential_energy >= Animal.MOVE_ENERGY:
            self._energy = potential_energy
            return True
        else:
            return False

    def eat(self, amount) -> int:
        potential_energy = self._energy + amount

        if potential_energy >= LivingThing.MAX_ENERGY:
            self._energy = LivingThing.MAX_ENERGY
            return potential_energy - LivingThing.MAX_ENERGY
        else:
            self._energy = potential_energy
            return self._energy - LivingThing.MAX_ENERGY

    def grow(self) -> None:
        self._age += 1

    def get_age(self) -> int:
        return self._age

    def reproduce(self) -> bool:
        potential_energy = self._energy - LivingThing.REPRODUCE_ENERGY

        if potential_energy >= LivingThing.MIN_ENERGY:
            self._energy = potential_energy
            return True
        else:
            return False
