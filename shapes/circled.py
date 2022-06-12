import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        perimeter = 2 * math.pi * float(self.radius)
        return perimeter

    def area(self):
        area = math.pi * float(self.radius) ** 2
        return area
