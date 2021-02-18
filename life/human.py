class Human:
    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        self.__name = name
        self.__age = age
        self.__energy = energy

    def __repr__(self) -> str:
        return f'human(name={self.__name}, age={self.__age}, energy={self.__energy})'

    def __str__(self) -> str:
        return f'{self.__name} is {self.__age} years old'

    def grow(self)->None:
        self.__age += 1

    def eat(self, amount) -> int:
        potential_energy = self.__energy + amount

        if potential_energy >= Human.MAX_ENERGY:
            self.__energy = Human.MAX_ENERGY
            return potential_energy - Human.MAX_ENERGY
        else:
            self.__energy = potential_energy
            return self.__energy - Human.MAX_ENERGY

    def reproduce(self) -> bool:
        potential_energy = self.__energy - Human.REPRODUCE_ENERGY

        if potential_energy >= Human.REPRODUCE_ENERGY:
            self.__energy = potential_energy
            return True
        else:
            return False

    def move(self, distance: int) -> bool:
        potential_energy = self.__energy - distance

        if potential_energy >= Human.MOVE_ENERGY:
            self.__energy = potential_energy
            return True
        else:
            return False
