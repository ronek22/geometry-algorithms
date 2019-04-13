class Area:

    def __init__(self, pmin: list, pmax: list):
        """
        Rectangle, pmin: leftbottom corner of rectangle
                   pmax: righttop corner of rectangle
        """
        if(len(pmin) !=2 or len(pmax) != 2):
            raise Exception("Listy musza byc dwuwymiarowe")

        if(pmin[0] > pmax[0] or pmin[1] > pmax[1]):
            raise Exception("pmin must be leftbottom corner of rectangle\npmax must be righttop corner of rectangle")
        self.pmin = pmin
        self.pmax = pmax

    def inside(self, point: tuple):
        if point[0] >= self.pmin[0] and point[1] >= self.pmin[1] and point[0] <= self.pmax[0] and point[1] <= self.pmax[1]:
            return True
        else:
            return False

    def intersect(self, region):
        # region is a set of points
        # returns true if any point lies inside
        for point in region:
            if self.inside(point):
                return True
        return False

    def contains(self, region):
        for point in region:
            if not self.inside(point):
                return False
        return True
    
    
    @property
    def bottomCorner(self):
        return self.pmin

    @property
    def topCorner(self):
        return self.pmax
        
    @property
    def width(self):
        return self.pmax[0] - self.pmin[0]

    @property
    def height(self):
        return self.pmax[1] - self.pmin[1]

    def __repr__(self):
        return "[X: {}, {} | Y: {}, {}]".format(self.pmin[0], self.pmax[0], self.pmin[1], self.pmax[1])