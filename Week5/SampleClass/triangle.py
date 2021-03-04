from shape import Shape


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        super().__init__("Triangle", 3)
        self.__base = base
        self.__height = height

    def __repr__(self):
        return f'Tritangle (sides={self._sides}, base={self.__base}, height={self.__height}'

    def calculate_area(self):
        return 0.5 * self.__base * self.__height
