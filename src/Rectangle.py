from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.name = "rectangle"

    @property
    def perimeter(self):
        return self.side1 + self.side2

    @property
    def area(self):
        return self.side1 * self.side2
