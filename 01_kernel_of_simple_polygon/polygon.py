from operator import attrgetter

class Polygon:

    def __init__(self, vertices):
        """Vertices have to store in counter clockwise order!"""
        self.vertices = vertices
        self.noOfVertices = len(vertices)
        self.bottomSpike = min(self.vertices, key=attrgetter('y'))
        self.topSpike = max(self.vertices, key=attrgetter('y'))
        if(vertices[-1] != vertices[0]):
            self.vertices.append(vertices[0])


    def orient_of_point(self, vertex):
        if (vertex >= self.noOfVertices):
            raise Exception("Given vertex doesn't exist")
        
        previous = self.vertices[vertex-1] if vertex != 0 else self.vertices[vertex-2]
        center = self.vertices[vertex]
        nextOne = self.vertices[vertex+1]
        needed = self.vertices[(vertex+2) % self.noOfVertices]

        x0,y0 = previous.get_xy
        x1,y1 = center.get_xy
        x2,y2 = nextOne.get_xy
        y3 = needed.y

        turn_right = (x2 - x0)*(y1 - y0) > (x1 - x0)*(y2 - y0)

        if turn_right:
            if y0 > y1 and y1 < y2:
                return 'top'
            elif y0 > y1 and y1 == y2:
                return 'top' if y3 > y2 else 0
            elif y0 < y1 and y1 > y2: 
                return 'bottom'
            elif y0 < y1 and y1 == y2:
                return 'bottom' if y3 < y2 else 0
        
        return 0


    def find_min_max(self):
        bottomSpikes = []
        topSpikes = []

        for i in range(0, self.noOfVertices):
            if(self.orient_of_point(i) == 'top'):
                topSpikes.append(self.vertices[i])
            elif(self.orient_of_point(i) == 'bottom'):
                bottomSpikes.append(self.vertices[i])

        if bottomSpikes:
            self.bottomSpike = max(bottomSpikes, key=attrgetter('y'))
        if topSpikes:
            self.topSpike = min(topSpikes, key=attrgetter('y'))

    def check_kernel(self):
        self.find_min_max()
        return self.topSpike.y >= self.bottomSpike.y


    def get_axes(self, axis=None):
        axis_x, axis_y = [p.x for p in self.vertices], [p.y for p in self.vertices]
        if axis == 'x':
            return axis_x
        elif axis == 'y': 
            return axis_y
        else: return axis_x, axis_y