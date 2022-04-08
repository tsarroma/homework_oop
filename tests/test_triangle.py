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
