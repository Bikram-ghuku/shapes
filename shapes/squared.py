class Square:
    def __init__(self, length):
        self.length = length
        diagonal = (2 * float(length) ** 2) ** 0.5
        self.diagonal = diagonal

    def area(self):
        area = float(self.length) ** 2
        return area

    def perimeter(self):
        perimeter = 4 * float(self.length)
        return perimeter
