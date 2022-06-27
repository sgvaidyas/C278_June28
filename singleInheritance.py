class Shape:
    def __init__(self):
        self.len = 0
        self.bred = 0
        self.rad = 0
    def setlen(self,l):
        self.len = l
    def setbred(self,b):
        self.bred = b
    def setrad(self,r):
        self.rad = r

class Square(Shape):
    def __init__(self):
        self.area = 0
        self.peri = 0

    def calculate(self):
        self.area = self.len**2
        self.peri = 4 * self.len

    def display(self):
        print("Area of square = ",self.area)
        print("Area of perimeter = ",self.peri)


ob = Square()
ob.setlen(9)
ob.calculate()
ob.display()
