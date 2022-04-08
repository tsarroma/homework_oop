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
