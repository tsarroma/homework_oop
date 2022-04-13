import pytest
from src.Figure import Figure
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture
def triangle_fixture():
    triangle1 = Triangle(20, 10, 22)
    return triangle1


@pytest.fixture
def square_fixture():
    square1 = Square(10)
    return square1


def test_triangle_name(triangle_fixture):
    name = triangle_fixture.name
    assert name == "triangle"


def test_triangle_perimeter(triangle_fixture):
    perimeter = triangle_fixture.perimeter
    assert perimeter == 52


def test_triangle_area(triangle_fixture):
    area = round(triangle_fixture.area)
    assert area == 100


def test_triangle_add_area(triangle_fixture, square_fixture):
    add_area = round(triangle_fixture.add_area(square_fixture))
    assert add_area == 200


def test_triangle_exception_cannot_created():
    with pytest.raises(ValueError) as excinfo:
        Triangle(0, 50, 100)
    assert 'Triangle cannot be created' == str(excinfo.value)


def test_triangle_exception_in_method_add_area():
    with pytest.raises(ValueError) as excinfo:
        triangle = Triangle(53, 50, 100)
        square = Square
        triangle.add_area(square)
    assert "Wrong class passed" == str(excinfo.value)


def test_triangle_isinstance_class_figure(triangle_fixture):
    triangle_class = isinstance(triangle_fixture, Figure)
    return triangle_class == True
