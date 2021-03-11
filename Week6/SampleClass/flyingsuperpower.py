from abc import ABC, abstractmethod

class FlyingSuperPower(ABC):
    @abstractmethod
    def fly(self, distance) -> None:
        raise NotImplementedError