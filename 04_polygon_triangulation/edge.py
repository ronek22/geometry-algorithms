from point import Point

class Edge:

    def __init__(self, p1: Point, p2: Point, color='b'):
        self.p1 = p1
        self.p2 = p2
        self.color = color
    
    def equation(self):
        if self.p1.x != self.p2.x:
            a = (self.p1.y - self.p2.y)/(self.p1.x - self.p2.x)
        else:
            a = 0
        b = self.p1.y - a * self.p1.x
        return a,b

    def __repr__(self):
        return f'Edges({self.p1} <-> {self.p2})'