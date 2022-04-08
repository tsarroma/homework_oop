import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
            self.name = "triangle"
        else:
            raise ValueError("Triangle cannot be created")

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def half_perimeter(self):
        return self.perimeter / 2

    @property
    def area(self):
        return round((math.sqrt(
            self.half_perimeter * (self.half_perimeter - self.side1) * (self.half_perimeter - self.side2) * (
                        self.half_perimeter - self.side3))), 2)
