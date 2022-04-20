import pytest
from src.Figure import Figure
from src.Circle import Circle
from src.Square import Square


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


def test_square_add_area(square_fixture, circle_fixture):
    add_area = square_fixture.add_area(circle_fixture)
    assert round(add_area) == 414


def test_square_isistance_class_figure(square_fixture):
    square_class = isinstance(square_fixture, Figure)
    return square_class == True
