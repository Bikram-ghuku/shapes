import math


class Ellipsoid:
    P: float = 1.6

    def __init__(self, major_axis: float, middle_axis: float, minor_axis: float):
        """
        An ellipsoid is a type of quadratic surface that is a higher dimensional analogue of an ellipse.
        It is similar to a sphere, except that the radii along one of the axis are longer than the radii
        along the other axis
        :param major_axis: The length along the X axis
        :param middle_axis:The length along the Y axis
        :param minor_axis: The length along the Z axis
        """
        self.a = major_axis
        self.b = middle_axis
        self.c = minor_axis

    def area(self):
        ab = (self.a * self.b) ** Ellipsoid.P
        ac = (self.a * self.c) ** Ellipsoid.P
        bc = (self.b * self.c) ** Ellipsoid.P
        return 4 * math.pi * ((ab + ac + bc) / 3) ** Ellipsoid.P ** -1

    def volume(self):
        return (4 / 3) * math.pi * self.a * self.b * self.c
