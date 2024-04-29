from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return sqrt(self.x ** 2 + self.y ** 2)


def distance(p1, p2):
    x_diff = p1.get_x() - p2.get_x()
    y_diff = p1.get_y() - p2.get_y()
    d = sqrt(x_diff ** 2 + y_diff ** 2)

    return d


p = Point(4, 3)
q = Point(1, 2)

print(p)
print(distance(p, q))
