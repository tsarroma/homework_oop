class Figure:

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            raise ValueError("Wrong class passed")

