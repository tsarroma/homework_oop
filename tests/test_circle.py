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


def test_circle_name(circle_fixture):
    name = circle_fixture.name
    assert name == "circle"


def test_circle_perimeter(circle_fixture):
    perimeter = circle_fixture.perimeter
    assert perimeter == 62.83


def test_circle_area(circle_fixture):
    area = circle_fixture.area
    assert area == 314.16


def test_circle_add_area(circle_fixture, square_fixture):
    add_area = circle_fixture.add_area(square_fixture)
    assert add_area == 414.16
