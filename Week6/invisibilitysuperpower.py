from abc import ABC, ABCMeta, abstractmethod


class InvisibilitySuperPower(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def turn_invisible(self) -> None:
        raise NotImplementedError

    def turn_visible(self) -> None:
        raise NotImplementedError
