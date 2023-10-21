class Rectangle():
    def __init__(self):
        self.width = 1
        self.length = 1
    def area(self):
        ar =  self.width * self.length
        print(ar)
    def perimeter(self):
        per = self.width * 2 + self.length * 2
        print(per)
    # def show(self, ar, per):
    #     print(ar, per)

recta = Rectangle()
recta.width = 10
recta.length = 5
recta.area()
recta.perimeter()


class Circle():
    def __init__(self):
        self.radius = 1
        self.pi = 3.14
    def area(self):
        ar =  self.pi * self.radius ** 2
        print(ar)
    def perimeter(self):
        per = 2 * self.pi * self.radius
        print(per)


circle = Circle()
circle.radius = 10
circle.area()
circle.perimeter()


class Triangle():
    def __init__(self):
        self.base = 1
        self.height = 1
    def area(self):
        ar = 0.5 * self.base * self.height
        print(ar)


tri = Triangle()
tri.base = 10
tri.height = 5
tri.area()
