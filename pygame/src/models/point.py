class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

    def __add__(self, other):
        if other is tuple:
            assert len(other) == 2
            self.shift(other[0], other[1])

    def to_tuple(self):
        return self.x, self.y
