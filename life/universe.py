from planet import Planet


class Universe:

    id =0

    def __init__(self):
        self.__planets = []

    def __repr__(self):
        return f'Universe (planets={len(self.__planets)})'

    def __str__(self):
        return f'The universe has (planets={len(self.__planets)}) planets.'

    def generate(self) -> Planet:
        Universe.id +=1
        planet = Planet(f"Planet {Universe.id}")
        self.__planets.append(planet)
        return planet

    def display(self) -> None:
        for planet in self.__planets:
            print(planet)

    def universe_size(self) -> int:
        return len(self.__planets)
