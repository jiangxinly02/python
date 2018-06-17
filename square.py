
import math

class Square:
    def __init__(self, l):
        self.length = l

    @property
    def perimeter(self):
        return self.length * 4

    @property
    def area(self):
        return self.length ** 2

    @perimeter.setter
    def perimeter(self, a):
        self.length = a / 4

    @area.setter
    def area(self,b):
        self.length = math.sqrt(b)


A = Square(2)
print(A.perimeter)
print(A.area)

