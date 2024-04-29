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

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def distance(self, other):
        x_diff = self.get_x() - other.get_x()
        y_diff = self.get_y() - other.get_y()
        d = sqrt(x_diff ** 2 + y_diff ** 2)

        return d


p = Point(1, 1)
q = Point(2, 2)

print(p)
print(p.distance(q))
