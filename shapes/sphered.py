import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 4 * math.pi * float(self.radius) ** 2
        return area

    def volume(self):
        volume = (4 / 3) * math.pi * float(self.radius) ** 3
        return volume
