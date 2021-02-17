from human import Human


class Planet:

    def __init__(self, name: str = '') -> None:
        self.__humans = []  # Private Attribute
        self.__name = name  # Private Attribute

    def __repr__(self):
        return f'planet(name={self.__name}, humans={self.__humans})'

    def __str__(self):
        return f'Planet {self.__name} has {len(self.__humans)} humans.'

    def add(self, human: Human) -> bool:
        self.__humans.append(human)
        return human in self.__humans

    def has(self, human: Human) -> bool:
        return human in self.__humans

    def population(self) -> int:
        return len(self.__humans)

    def remove(self, human: Human) -> bool:
        self.__humans.remove(human)
        return human in self.__humans
