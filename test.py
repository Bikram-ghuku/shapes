import pytest
import shapes

rectangle = shapes.rectangle(16, 18)
square = shapes.square(2)
circle = shapes.circle(7)
tangle = shapes.triangle(A=2, B=3, C=3)
sphere = shapes.sphere(5)


def test_rectrangle_perimeter():
    assert rectangle.perimeter == 68.0, "test failed"
    assert type(rectangle.perimeter) == float, "datatype error"


def test_rectangle_area():
    assert rectangle.area == 288.0, "test failed"
    assert type(rectangle.area) == float, "datatype error"


def test_square_area():
    assert square.area == 4.0, "test failed"
    assert type(square.area) == float, "datatype error"


def test_square_perimeter():
    assert square.perimeter == 8.0, "test failed"
    assert type(square.perimeter) == float, "datatype error"


def test_circle_perimeter():
    assert circle.perimeter == 43.982297150257104, "test failed"
    assert type(circle.perimeter) == float, "datatype error"


def test_circle_area():
    assert circle.area == 153.93804002589985, "test failed"
    assert type(circle.area) == float, "datatype error"


def test_triangle_area():
    assert tangle.perimeter == 8.0, "test failed"
    assert type(tangle.perimeter) == float, "datatype error"


def test_sphere_area():
    assert sphere.area == 314.1592653589793, "test failed"
    assert type(sphere.area) == float, "datatype error"


def test_sphere_volume():
    assert sphere.volume == 523.5987755982989, "test failed"
    assert type(sphere.volume) == float, "datatype error"
