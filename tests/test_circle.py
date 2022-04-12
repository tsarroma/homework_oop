import pytest
from src.Figure import Figure
from src.Circle import Circle


@pytest.fixture
def circle1_fixture():
    circle1 = Circle(10)
    return circle1

@pytest.fixture
def circle2_fixture():
    circle2 = Circle(20)
    return circle2

def test_circle_name(circle1_fixture):
    name = circle1_fixture.name
    assert name == "circle"


def test_circle_perimeter(circle1_fixture):
    perimeter = circle1_fixture.perimeter
    assert perimeter == 62.83


def test_circle_area(circle1_fixture):
    area = circle1_fixture.area
    assert area == 314.16


def test_circle_add_area(circle1_fixture, circle2_fixture):
    add_area = circle1_fixture.add_area(circle2_fixture)
    assert round(add_area) == 1571

def test_circle_isistance_class_figure(circle1_fixture):
    circle_class = isinstance(circle1_fixture, Figure)
    return circle_class == True
