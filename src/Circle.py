import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        if radius == 0:
            return ValueError("fff")
        self.name = "circle"


    @property
    def perimeter(self):
        return round((2 * math.pi * self.radius), 2)

    @property
    def area(self):
        return round((math.pi * self.radius ** 2), 2)
