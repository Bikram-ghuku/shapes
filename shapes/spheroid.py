import math


class Spheroid:
    # spheroid is a sphere with semi-axis (a, a, c)
    def __init__(self, semi_axis_a, semi_axis_c):
        self.semi_axis_a = semi_axis_a
        self.semi_axis_c = semi_axis_c

    def area(self):
        if self.semi_axis_c < self.semi_axis_a:
            e = math.sqrt(1 - self.semi_axis_c**2 / self.semi_axis_a**2)
            area = (
                2 * math.pi * self.semi_axis_a**2
                + math.pi
                * self.semi_axis_c**2
                / e
                * math.log((1 + e) / (1 - e), math.e)
            )
        else:
            e = math.sqrt(1 - self.semi_axis_a**2 / self.semi_axis_c**2)
            area = (
                2
                * math.pi
                * self.semi_axis_a**2
                * (1 + self.semi_axis_c / (self.semi_axis_a * e) * math.asin(e))
            )
        return area

    def volume(self):
        volume = (4 / 3) * math.pi * float(self.semi_axis_a) ** 2 * self.semi_axis_c
        return volume
