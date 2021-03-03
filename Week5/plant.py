from livingthing import LivingThing

class Plant(LivingThing):
    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name: str) -> None:
        self.__name = name

    def __repr__(self) -> str:
        return f'plant (name={self.__name})'

    def __str__(self) -> str:
        return f'{self.__name} is a plant'

    def absorb(self, energy: int) -> int:
        potential_energy = energy
        return potential_energy
