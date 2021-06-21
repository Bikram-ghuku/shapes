import math

class rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area_op = int(self.height)*int(self.width)
        return area_op

    def perimeter(self):
        perimeter = 2*(int(self.height) + int(self.width))
        return perimeter

class square():
    def __init__(self, length):
        self.length = length
    
    def area(self):
        area = int(self.length)**2
        return area

    def perimeter(self):
        perimeter = 4*int(self.length)
        return perimeter

class circle():
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        perimeter = 2*math.pi*int(self.radius)
        return perimeter

    def area(self):
        area = math.pi*int(self.radius)**2
        return area