from planet import Planet


class Universe:

    def __init__(self):
        self.__planets = []

    def generate(self, planet: Planet) -> Planet:
        planet = Planet()
        self.__planets.append(planet)
        return planet

    def display(self) -> None:
        for planet in self.__planets:
            print (planet)

    def universe_size(self) -> int:
        return len(self.__planets)
