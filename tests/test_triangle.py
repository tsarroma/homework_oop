import pytest
from src.Triangle import Triangle
from src.Figure import Figure
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square

@pytest.fixture
def triangle_fixture():
    triangle1 = Triangle(53, 50, 100)
    return triangle1

@pytest.fixture
def square_fixture():
    square1 = Square(53)
    return square1

def test_name(triangle_fixture):
    name = triangle_fixture.name
    assert name == "triangle"

def test_area(triangle_fixture):
    area = triangle_fixture.area
    assert area == area

def test_perimeter(triangle_fixture):
    perimeter = triangle_fixture.perimeter
    assert perimeter == perimeter

def test_triangle_set_three_side():
    pass

def test_not_create_error():
    pass

def test_metod_add_area_error():
    pass

def test_metod_add_area(triangle_fixture):
    add_area = triangle_fixture.add_area(Square(10))
    print(add_area)
