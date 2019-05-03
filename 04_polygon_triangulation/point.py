from math import atan2, pi, degrees

class Point:
    def __init__(self, x=0, y=0, orientation=1):
        self.x = x
        self.y = y
        self.orientation = orientation


    def angle_three_points(self, p2, p3):
        rads = atan2(p2.y - self.y, p2.x - self.x) - atan2(p3.y - self.y, p3.x - self.x)
        rads %= 2*pi
        out = degrees(rads)
        print(out)
        return out

    def turn_right(self, p2, p3):
        return (p3.x - self.x)*(p2.y - self.y) >= (p2.x - self.x)*(p3.y - self.y)

    @property
    def get_xy(self):
        return self.x, self.y

    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
        