import pytest
import math
import shapes
import sentry_sdk

sentry_sdk.init(
    dsn="https://8fddf93bdb044fb7b551c14158df85e7@o1272929.ingest.sentry.io/6467004",
    traces_sample_rate=1.0)

rectangle = shapes.Rectangle(16, 18)
square = shapes.Square(2)
circle = shapes.Circle(7)
tangle = shapes.Triangle(A=2, B=3, C=3)
sphere = shapes.Sphere(5)
ellipse = shapes.Ellipse(20, 10)
cylinder = shapes.Cylinder(3, 10)
spheroid_a_less_c = shapes.Spheroid(5, 14)
spheroid_c_less_a = shapes.Spheroid(14, 5)


def test_rectangle_perimeter():
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


def test_ellipse_perimeter():
    assert round(ellipse.perimeter, 4) == 96.8845, "test failed"
    assert type(ellipse.perimeter) == float, "datatype error"


def test_ellipse_area():
    assert ellipse.area == math.pi * 200, "test failed"
    assert type(ellipse.area) == float, "datatype error"


def test_cylinder_volume():
    assert cylinder.volume == math.pi * 90, "test failed"
    assert type(cylinder.volume) == float, "datatype error"


def test_cylinder_total_surf_area():
    assert cylinder.total_surface_area == math.pi * 78, "test failed"
    assert type(cylinder.total_surface_area) == float, "datatype error"


def test_cylinder_lateral_surf_area():
    assert cylinder.lateral_surface_area == math.pi * 60, "test failed"
    assert type(cylinder.total_surface_area) == float, "datatype error"


def test_spheroid_volume():
    assert round(spheroid_a_less_c.volume, 5) == 1466.07657, "test failed"
    assert round(spheroid_c_less_a.volume, 5) == 4105.01440, "test failed"
    assert type(spheroid_a_less_c.volume) == float, "datatype error"
    assert type(spheroid_c_less_a.volume) == float, "datatype error"


def test_spheroid_area_a_less_c():
    assert round(spheroid_a_less_c.area, 5) == 724.76435, "test failed"
    assert type(spheroid_a_less_c.area) == float, "datatype error"


def test_spheroid_area_c_less_a():
    assert round(spheroid_c_less_a.area, 5) == 1515.58393, "test failed"
    assert type(spheroid_c_less_a.area) == float, "datatype error"
