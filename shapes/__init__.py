from . import squared, circled, triangled, rectangled, cylindered, sphered, ellipsed


class square(squared.square):
    def __init__(self, length):
        super().__init__(length)
        self.area = squared.square(length).area()
        self.perimeter = squared.square(length).perimeter()


class circle(circled.circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.area = circled.circle(radius).area()
        self.perimeter = circled.circle(radius).perimeter()


class triangle(triangled.triangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.area = triangled.triangle(**kwargs).area()
        self.perimeter = triangled.triangle(**kwargs).perimeter()


class rectangle(rectangled.rectangle):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.area = rectangled.rectangle(height, width).area()
        self.perimeter = rectangled.rectangle(height, width).perimeter()


class cylinder(cylindered.cylinder):
    def __init__(self, radius, height):
        super().__init__(radius, height)
        self.lateralSurfaceArea = cylindered.cylinder(
            radius, height
        ).lateralSurfaceArea()
        self.totalSurfaceArea = cylindered.cylinder(radius, height).totalSurfaceArea()
        self.volume = cylindered.cylinder(radius, height).volume()


class sphere(sphered.sphere):
    def __init__(self, radius):
        super().__init__(radius)
        self.area = sphered.sphere(radius).area()
        self.volume = sphered.sphere(radius).volume()


class ellipse(ellipsed.ellipse):
    def __init__(self, major_semiaxis, minor_semiaxis):
        super().__init__(major_semiaxis, minor_semiaxis)
        self.perimeter = ellipsed.ellipse(major_semiaxis, minor_semiaxis).perimeter()
        self.area = ellipsed.ellipse(major_semiaxis, minor_semiaxis).area()
