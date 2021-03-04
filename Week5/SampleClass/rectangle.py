from shape import Shape

class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        super().__init__("Rectangle", 4)
        self.__length = length
        self.__width = width

    def __repr__(self):
        return f'Rectangle (sides={self._sides}, length={self.__length}), width={self.__width}'


    def calcualte_area(self):
        return self.__width*self.__length
