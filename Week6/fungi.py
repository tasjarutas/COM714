from livingthing import LivingThing


class Fungi(LivingThing):
    REPRODUCE_ENERGY = 5
    MIN_ENERGY = 1

    def __init__(self, name: str, age: int = 0, energy: int = LivingThing.MAX_ENERGY) -> None:
        super().__init__(name, age, energy)

    def __repr__(self) -> str:
        return f'Fungi (name={self._name}, age={self._age}, energy={self._energy})'

    def __str__(self) -> str:
        return f'{self._name} is {self._age} years old and has an energy of {self._energy}.'

    def absorb(self, amount: int) -> int:
        potential_energy = self._energy+amount
        if potential_energy >= LivingThing.MAX_ENERGY:
            self._energy = LivingThing.MAX_ENERGY
            return potential_energy - LivingThing.MAX_ENERGY
        else:
            self._energy = potential_energy
            return self._energy - LivingThing.MAX_ENERGY

    def reproduce(self) -> bool:
        potential_energy = self._energy - LivingThing.REPRODUCE_ENERGY

        if potential_energy >= LivingThing.MIN_ENERGY:
            self._energy = potential_energy
            return True
        else:
            return False
