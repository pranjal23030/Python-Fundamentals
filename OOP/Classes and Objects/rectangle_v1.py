from math import sqrt


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"x={self.x}, y={self.y}"

    def distance(self, other):
        x_diff = self.get_x() - other.get_x()
        y_diff = self.get_y() - other.get_y()
        d = sqrt(x_diff ** 2 + y_diff ** 2)

        return d

    ##p = Point(4, 3)


##q = Point(0, 0)
##
##print(p.distance(q))

class Rectangle:
    def __init__(self, corner=Point(0.0, 0.0), length=200, breadth=100):
        self.corner = corner
        self.length = length
        self.breadth = breadth

    def grow(self, l, b):
        self.length += l
        self.breadth += b

    def center(self):
        c = Point()
        c.x = self.corner.x + self.length / 2
        c.y = self.corner.y + self.breadth / 2
        return c


r = Rectangle()
print(r.center())
r.grow(50, 20)
print(r.length)
print(r.breadth)
