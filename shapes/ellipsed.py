import math
from scipy import integrate


def fully_int_second(t, k):
    return math.sqrt(1 - (k**2) * (math.sin(t) ** 2))


class Ellipse:
    def __init__(self, major_semi_axis, minor_semi_axis):
        self.a = major_semi_axis
        self.b = minor_semi_axis

    def perimeter(self):
        eccentricity = math.sqrt((self.a * 2) ** 2 - (self.b * 2) ** 2) / (self.a * 2)
        fully_ellipse_int_second, err = integrate.quad(
            fully_int_second, 0, math.pi / 2, args=eccentricity
        )
        perimeter = 4 * self.a * fully_ellipse_int_second
        return perimeter

    def area(self):
        area = math.pi * self.a * self.b
        return area
