import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

@pytest.fixture
def triangle_fixture():
    triangle1 = Triangle(20, 10, 22)
    return triangle1

@pytest.fixture
def rectangle_fixture():
    rectangle1 = Rectangle(10, 20)
    return rectangle1

@pytest.fixture
def square_fixture():
    square1 = Square(10)
    return square1

@pytest.fixture
def circle_fixture():
    circle1 = Circle(10)
    return circle1


def test_square_name(square_fixture):
    name = square_fixture.name
    assert name == "square"


def test_square_perimeter(square_fixture):
    perimeter = square_fixture.perimeter
    assert perimeter == 20


def test_square_area(square_fixture):
    area = square_fixture.area
    assert area == 100


def test_square_add_area(square_fixture):
    add_area = square_fixture.add_area(square_fixture)
    assert add_area == 200
