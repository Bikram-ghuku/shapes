class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        diagonal = (float(height) ** 2 + float(width) ** 2) ** 0.5
        self.diagonal = diagonal

    def area(self):
        area_op = float(self.height) * float(self.width)
        return area_op

    def perimeter(self):
        perimeter = 2 * (float(self.height) + float(self.width))
        return perimeter
