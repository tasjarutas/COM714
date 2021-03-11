from abc import ABC, ABCMeta, abstractmethod

class SpeedSuperPower(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run_fast(self, distance)->None:
        raise NotImplementedError
