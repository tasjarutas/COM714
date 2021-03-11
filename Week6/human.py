from clothing import Clothing
from animal import Animal


class Human(Animal):
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name: str, age: int = 0, energy: int = Animal.MAX_ENERGY) -> None:
        super().__init__(name, age, energy)
        self.__clothing = []

    def dress(self, clothing: Clothing):
        self.__clothing.append(clothing)

    def number_dress(self) -> int:
        return len(self.__clothing)

    def undress(self, clothing: Clothing):
        self.__clothing.remove(clothing)
