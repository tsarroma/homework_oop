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


def test_triangle_name(triangle_fixture):
    name = triangle_fixture.name
    assert name == "triangle"


def test_triangle_perimeter(triangle_fixture):
    perimeter = triangle_fixture.perimeter
    assert perimeter == 52


def test_triangle_area(triangle_fixture):
    area = triangle_fixture.area
    assert area == 99.91


def test_triangle_add_area(triangle_fixture):
    add_area = triangle_fixture.add_area(triangle_fixture)
    assert add_area == 199.84


def test_triangle_area(triangle_fixture, square_fixture):
    area = triangle_fixture.area
    assert area == area


def test_triangle_perimeter(triangle_fixture):
    perimeter = triangle_fixture.perimeter
    assert perimeter == perimeter


def test_triangle_set_three_side():
    pass


def test_triangle_not_create_error():
    pass


def test_triangle_metod_add_area_error():
    pass


def test_metod_add_area(triangle_fixture):
    add_area = triangle_fixture.add_area(Square(10))
    print(add_area)
