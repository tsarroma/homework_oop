def test_square_name(square_fixture):
    name = square_fixture.name
    assert name == "square"


def test_square_perimeter(square_fixture):
    perimeter = square_fixture.perimeter
    assert perimeter == 20


def test_square_area(square_fixture):
    area = square_fixture.area
    assert area == 100


def test_square_add_area(square_fixture):
    add_area = square_fixture.add_area(square_fixture)
    assert add_area == 200
