import pytest
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.fixture
def rectangle_fixture():
    rectangle1 = Rectangle(10, 20)
    return rectangle1


@pytest.fixture
def square_fixture():
    square1 = Square(10)
    return square1


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


def test_rectangle_isistance_class_figure(rectangle_fixture):
    rectangle_class = isinstance(rectangle_fixture, Figure)
    return rectangle_class == True
