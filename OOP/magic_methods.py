class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x, self.y})'

    def __str__(self):
        return f'Class: Point2D,' \
            f' x: {self.x}, y: {self.y}'

    def __add__(self, other):
        if isinstance(self, other.__class__):
            return Point2D(self.x + other.x, self.y + other.y)
        else:
            return None

    def __sub__(self, other):
        if isinstance(self, other.__class__):
            return Point2D(self.x - other.x, self.y - other.y)
        else:
            return None

p1 = Point2D(2, 3)
p2 = Point2D(4, 5)
#
# print(p1)
#
# print(repr(p2))
# print(str(p2))

p3 = p1+p2
print(p3)
print(p2-p1)
