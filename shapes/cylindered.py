import math


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def lateral_surface_area(self):
        lateral_surface_area = 2 * math.pi * float(self.radius * self.height)
        return lateral_surface_area

    def total_surface_area(self):
        total_surface_area = (
            2 * math.pi * float(self.radius * self.height)
            + 2 * math.pi * float(self.radius) ** 2
        )
        return total_surface_area

    def volume(self):
        volume = math.pi * float(self.radius) ** 2 * self.height
        return volume
