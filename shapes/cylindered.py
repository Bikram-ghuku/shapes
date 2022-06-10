import math

class cylinder():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def lateralSurfaceArea(self):
        lateralSurfaceArea = 2*math.pi*float(self.radius * self.height)
        return lateralSurfaceArea

    def totalSurfaceArea(self):
        totalSurfaceArea = 2*math.pi*float(self.radius*self.height) + 2*math.pi*float(self.radius)**2
        return totalSurfaceArea

    def volume(self):
        volume = math.pi*float(self.radius)**2*self.height
        return volume