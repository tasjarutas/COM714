from planet import Planet
from non_planet import NonPlanet
from typing import List
import random


class Universe:
    id = 0

    def __init__(self):
        self.__planets = []
        self.__non_planets = []

    def __repr__(self):
        return f'Universe (planets={len(self.__planets)})'

    def __str__(self):
        return f'The universe has (planets={len(self.__planets)}) planets.'

    def generate_planet(self, planet_names: List[str]) -> None:
        generated_planets = []
        Universe.id += 1

        for planet_name in planet_names:
            planet = Planet(planet_name)
            self.__planets.append(planet)
            #generated_planets.append(planet)

    def generate_non_planet(self, non_planet_names: List[str]) -> None:
        for non_planet_name in non_planet_names:
            non_planet = NonPlanet(non_planet_name)
            self.__non_planets.append(non_planet)

    def display(self) -> None:
        for planet in self.__planets:
            print(planet)

    def universe_size(self) -> int:
        return len(self.__planets)
