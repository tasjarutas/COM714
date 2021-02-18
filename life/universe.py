from planet import Planet
from non_planet import NonPlanet
import random


class Universe:
    id = 0

    def __init__(self):
        self.__planets = []

    def __repr__(self):
        return f'Universe (planets={len(self.__planets)})'

    def __str__(self):
        return f'The universe has (planets={len(self.__planets)}) planets.'

    def generate(self) -> None:
        Universe.id += 1

        if random.randint(0, 10) >=5:
            planet = Planet(f"Planet {Universe.id}")
            self.__planets.append(planet)
        else:
            non_planet = NonPlanet(f"NonPlanet {Universe.id}")
            self.__planets.append(non_planet)

    def display(self) -> None:
        for planet in self.__planets:
            print(planet)

    def universe_size(self) -> int:
        return len(self.__planets)
