from clothing_size import ClothingSize

class Clothing:

    def __init__(self, colour:str, material:str, clothing_size: ClothingSize) -> None:
        self.__colour = colour
        self.__material = material
        self.__size = clothing_size
        self.__cloths = []

    def __repr__(self) -> str:
        return f'clothing(colour={self.__colour}, material={self.__material}, size={self.__size})'

    def __str__(self) -> str:
        return f'This {self.__material} is {self.__colour} and is {self.__size}.'

    def get_colour(self)-> str:
        return f'The colour of cloth is {self.__colour}'
