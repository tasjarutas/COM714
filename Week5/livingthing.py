class LivingThing:
    REPRODUCE_ENERGY = 20
    MAX_ENERGY = 100

    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        self.__name = name
        self.__age = age
        self.__energy = energy

    def __repr__(self) -> str:
        return f'living_thing (name={self.__name}, age={self.__age}, energy={self.__energy})'

    def __str__(self) -> str:
        return f'{self.__name} is {self.__age} years old'

    def grow(self) -> None:
        self.__age += 1

    def reproduce(self) -> bool:
        potential_energy = self.__energy - LivingThing.REPRODUCE_ENERGY

        if potential_energy >= LivingThing.REPRODUCE_ENERGY:
            self.__energy = potential_energy
            return True
        else:
            return False
