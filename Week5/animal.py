from livingthing import LivingThing


class Animal(LivingThing):
    MAX_ENERGY = 100
    MIN_ENERGY = 0
    REPRODUCE_ENERGY = 1

    def __init__(self, name: str, age: int = 0, energy: int = LivingThing.MAX_ENERGY) -> None:
        self.__name = name
        self.__age = age
        self.__energy = energy

    def __repr__(self) -> str:
        return f'animal(name={self.__name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.__name} is {self.age} years old and has an energy of {self.energy}.'

    def move(self, distance: int) -> bool:
        potential_energy = self.__energy - distance

        if potential_energy >= Animal.MOVE_ENERGY:
            self.__energy = potential_energy
            return True
        else:
            return False

    def eat(self, amount) -> int:
        potential_energy = self.__energy + amount

        if potential_energy >= Animal.MAX_ENERGY:
            self.__energy = Animal.MAX_ENERGY
            return potential_energy - Animal.MAX_ENERGY
        else:
            self.__energy = potential_energy
            return self.__energy - Animal.MAX_ENERGY

    def grow(self) -> None:
        self.__age += 1

    def get_age(self) -> int:
        return self.__age

    def reproduce(self) -> bool:
        potential_energy = self.__energy - Animal.REPRODUCE_ENERGY

        if potential_energy >= Animal.MIN_ENERGY:
            self.__energy = potential_energy
            return True
        else:
            return False
