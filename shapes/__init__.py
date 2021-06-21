import math

class rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        diagonal = (float(height)**2 + float(width)**2)**0.5
        self.diagonal = diagonal

    def area(self):
        area_op = float(self.height)*float(self.width)
        return area_op

    def perimeter(self):
        perimeter = 2*(float(self.height) + float(self.width))
        return perimeter

class square():
    def __init__(self, length):
        self.length = length
        diagonal  = (2*float(length)**2)**0.5 
        self.diagonal = diagonal
    
    def area(self):
        area = float(self.length)**2
        return area

    def perimeter(self):
        perimeter = 4*float(self.length)
        return perimeter

class circle():
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = self.perimeter()
        self.area = self.area()

    def perimeter(self):
        perimeter = 2*math.pi*float(self.radius)
        return perimeter

    def area(self):
        area = math.pi*float(self.radius)**2
        return area

sides = []
class triangle():
    def __init__(self, **kwargs):
        self.len = len(kwargs)
        if self.len == 3:
            self.a = kwargs['A']
            self.b = kwargs['B']
            self.c = kwargs['C']
            self.semi_perimeter = (float(self.a) + float(self.b) + float(self.c))/2
        elif self.len == 2:
            self.base = kwargs['base']
            self.height = kwargs['height']

    def area(self):
        if self.len == 2:
            area = 1/2*float(self.base)*float(self.height)
        elif self.len == 3:
            x_a = self.semi_perimeter - self.a
            x_b = self.semi_perimeter - self.b
            x_c = self.semi_perimeter - self.c
            area = (float(self.semi_perimeter) * float(x_a) * float(x_b) * float(x_c))**0.5

        return area
