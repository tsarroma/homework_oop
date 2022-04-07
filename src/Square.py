from src.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side1):
        super().__init__( side1, side2=0)
        self.name = "square"

    @property
    def perimeter(self):
        return self.side1 + self.side1

    @property
    def area(self):
        return self.side1 ** 2

