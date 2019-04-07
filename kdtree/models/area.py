from models.point import Point

class Area:

    def __init__(self, pmin: Point, pmax: Point):
        """
        Rectangle, pmin: leftbottom corner of rectangle
                   pmax: righttop corner of rectangle
        """

        self.pmin = pmin
        self.pmax = pmax

    def is_inside(self, point: tuple):
        if point[0] > self.pmin.x and point[1] > self.pmin.y and point[0] < self.pmax.x and point[1] < self.pmax.y:
            print("INSIDE:", point)
            return True
        else:
            return False
        