class Shape:
    def __init__(self, name: str, side: int = 0) -> None:
        self._name = name
        self._side = side

    def __repr__(self) -> str:
        return f'Shape(name={self._name}, side={self._sides})'

    def __str__(self) -> str:
        return f'{self._name} has {self._sides} sides.'
