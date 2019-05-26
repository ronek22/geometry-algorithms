from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.dist = None

    @property
    def get_xy(self):
        return self.x, self.y

    def get_distance(self, p2):
        return sqrt((p2.x-self.x)**2 + (p2.y - self.y)**2)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
