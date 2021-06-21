import math

class rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.diagonal = (float(height)**2 + float(width)**2)**0.5

    def area(self):
        area_op = float(self.height)*float(self.width)
        return area_op

    def perimeter(self):
        perimeter = 2*(float(self.height) + float(self.width))
        return perimeter

class square():
    def __init__(self, length):
        self.length = length
        self.diagonal = (2*float(length)**2)**0.5
    
    def area(self):
        area = float(self.length)**2
        return area

    def perimeter(self):
        perimeter = 4*float(self.length)
        return perimeter

class circle():
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        perimeter = 2*math.pi*float(self.radius)
        return perimeter

    def area(self):
        area = math.pi*float(self.radius)**2
        return area