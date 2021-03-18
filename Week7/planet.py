# from human import Human
from livingthing import LivingThing


class Planet:

    def __init__(self, name: str = '') -> None:
        self.__living_things = []  # Private Attribute
        self.__name = name  # Private Attribute

    def __repr__(self):
        return f'planet(name={self.__name}, living_things={self.__living_things})'

    def __str__(self):
        return f'The Planet {self.__name} has {len(self.__living_things)} living things.'

    def add(self, living_thing: LivingThing) -> bool:
        self.__living_things.append(living_thing)
        return living_thing in self.__living_things

    def has(self, living_thing: LivingThing) -> bool:
        return living_thing in self.__living_things

    def population(self) -> int:
        return len(self.__living_things)

    def remove(self, living_thing: LivingThing) -> bool:
        self.__living_things.remove(living_thing)
        return living_thing in self.__living_things

    # Human class is an attribute of planet
    # def __init__(self, name: str = '') -> None:
    #     self.__humans = []  # Private Attribute
    #     self.__name = name  # Private Attribute
    #
    # def __repr__(self):
    #     return f'planet(name={self.__name}, humans={self.__humans})'
    #
    # def __str__(self):
    #     return f'The Planet {self.__name} has {len(self.__humans)} humans.'
    #
    # def add(self, human: Human) -> bool:
    #     self.__humans.append(human)
    #     return human in self.__humans
    #
    # def has(self, human: Human) -> bool:
    #     return human in self.__humans
    #
    # def population(self) -> int:
    #     return len(self.__humans)
    #
    # def remove(self, human: Human) -> bool:
    #     self.__humans.remove(human)
    #     return human in self.__humans
