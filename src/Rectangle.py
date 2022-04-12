from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.name = "rectangle"
        if side1 > 0 and side2 >= 0:
            self.side1 = side1
            self.side2 = side2
        else:
            raise ValueError("Side must be greater than zero")

    @property
    def perimeter(self):
        return self.side1 + self.side2

    @property
    def area(self):
        return self.side1 * self.side2
