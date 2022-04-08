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
