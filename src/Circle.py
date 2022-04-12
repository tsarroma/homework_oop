import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.name = "circle"
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("Radius must be greater than zero")

    @property
    def perimeter(self):
        return round((2 * math.pi * self.radius), 2)

    @property
    def area(self):
        return round((math.pi * self.radius ** 2), 2)
