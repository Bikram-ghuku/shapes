class Triangle:
    def __init__(self, **kwargs):
        self.lend = len(kwargs)
        self.a = kwargs["A"]
        self.b = kwargs["B"]
        self.c = kwargs["C"]
        semi_perimeter = (float(self.a) + float(self.b) + float(self.c)) / 2
        self.semi_perimeter = semi_perimeter

    def area(self):
        if self.lend == 3:
            x_a = self.semi_perimeter - self.a
            x_b = self.semi_perimeter - self.b
            x_c = self.semi_perimeter - self.c
            area = (
                float(self.semi_perimeter) * float(x_a) * float(x_b) * float(x_c)
            ) ** 0.5
        else:
            raise Exception(
                "Input should either be of length 3 , Received: {}".format(self.lend)
            )
        return area

    def perimeter(self):
        if self.lend == 3:
            perimeter = float(self.a) + float(self.b) + float(self.c)
        else:
            raise Exception(
                "Unidentified input, perimeter requires 3 inputs recived {}".format(
                    self.lend
                )
            )

        return perimeter
