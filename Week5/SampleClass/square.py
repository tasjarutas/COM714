from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,length: float):
        super().__init__(length,length)
