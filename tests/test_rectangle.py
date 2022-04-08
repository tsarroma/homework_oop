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


def test_rectangle_name(rectangle_fixture):
    name = rectangle_fixture.name
    assert name == "rectangle"


def test_rectangle_perimeter(rectangle_fixture):
    perimeter = rectangle_fixture.perimeter
    assert perimeter == 30


def test_rectangle_area(rectangle_fixture):
    area = rectangle_fixture.area
    assert area == 200


def test_rectangle_add_area(rectangle_fixture, square_fixture):
    add_area = rectangle_fixture.add_area(square_fixture)
    assert add_area == 300
