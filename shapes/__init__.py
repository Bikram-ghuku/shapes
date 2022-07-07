from . import (
    squared,
    circled,
    triangled,
    rectangled,
    cylindered,
    sphered,
    ellipsed,
    spheroid,
    ellipsoid
)


class Square(squared.Square):
    def __init__(self, length):
        super().__init__(length)
        self.area = super().area()
        self.perimeter = super().perimeter()


class Circle(circled.Circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.area = super().area()
        self.perimeter = super().perimeter()


class Triangle(triangled.Triangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.area = super().area()
        self.perimeter = super().perimeter()


class Rectangle(rectangled.Rectangle):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.area = super().area()
        self.perimeter = super().perimeter()


class Cylinder(cylindered.Cylinder):
    def __init__(self, radius, height):
        super().__init__(radius, height)
        self.lateral_surface_area = super().lateral_surface_area()
        self.total_surface_area = super().total_surface_area()
        self.volume = super().volume()


class Sphere(sphered.Sphere):
    def __init__(self, radius):
        super().__init__(radius)
        self.area = super().area()
        self.volume = super().volume()


class Ellipse(ellipsed.Ellipse):
    def __init__(self, major_semi_axis, minor_semi_axis):
        super().__init__(major_semi_axis, minor_semi_axis)
        self.perimeter = super().perimeter()
        self.area = super().area()


class Spheroid(spheroid.Spheroid):
    def __init__(self, semi_axis_a, semi_axis_c):
        super().__init__(semi_axis_a, semi_axis_c)
        self.area = super().area()
        self.volume = super().volume()

class Ellipsoid(ellipsoid.Ellipsoid):
    def __init__(self, major_axis: float, middle_axis: float, minor_axis: float):
        super.__init__(major_axis, middle_axis, minor_axis)
        self.area = super().area()
        self.volume = super().volume()