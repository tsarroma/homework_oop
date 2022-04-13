from src.Figure import Figure


class Square(Figure):
    def __init__(self, side1):
        self.name = "square"
        if side1 > 0:
            self.side1 = self.side2 = side1
        else:
            raise ValueError("Square sides must be greater than 0.")

    @property
    def perimeter(self):
        return self.side1 + self.side1

    @property
    def area(self):
        return self.side1 ** 2
