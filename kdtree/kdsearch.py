class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def get_xy(self):
        return (self.x, self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

class Node: 
    def __init__(self, data=None, division=None, left=None, right=None):
        self.data = data
        self.division = division
        self.left = left
        self.right = right

    @property
    def children(self):
        """ 
        Returns iterator for children, return as (Node, pos) where
        pos = 0 for the left subnode and pos = 1 for the right.
        """

        if self.left and self.left.data is not None:
            yield self.left, 0
        if self.right and self.right.data is not None:
            yield self.right, 1

    def set_child(self, index, child):
        """ Sets one of the node's children, index = 0 for left, 1 for right"""
        if index == 0:
            self.left = child
        else:
            self.right = child

    def get_child_pos(self,child):
        for c, pos in self.children:
            if child == c:
                return pos

    def preorder(self):
        """Preorder traverse tree, root, left, right"""

        if not self:
            return

        yield self

        if self.left:
            for x in self.left.preorder():
                yield x
        
        if self.right:
            for x in self.right.preorder():
                yield x

    def inorder(self):
        """ iterator for nodes: left, root, right """

        if not self:
            return

        if self.left:
            for x in self.left.inorder():
                yield x

        yield self

        if self.right:
            for x in self.right.inorder():
                yield x

    def height(self):
        min_height = int(bool(self))
        return max([min_height] + [c.height()+1 for c, p in self.children])

    def __repr__(self):
        return '<%(cls)s - %(data)s>' % \
        dict(cls=self.__class__.__name__, data=repr(self.data))


    def __bool__(self):
        return self.data is not None


    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.data == other
        else:
            return self.data == other.data

    def __hash__(self):
        return id(self)

class Area:
    def __init__(self, maxpoint: Point, minpoint: Point):
        self.maxpoint = maxpoint
        self.minpoint = minpoint

def buildTree(points, height):
    size = len(points)
    half = size >> 1

    if size == 1:
        return Node(points[0], points[0])
    elif height % 2 == 0:
        tab = sorted(points, key=lambda point: point.x)
    else:
        tab = sorted(points, key=lambda point: point.y)

    L = tab[:half]
    R = tab[half + 1:]
    try:
        return Node(points[half], tab[half],
            buildTree(L, height+1),
            buildTree(R, height+1)
    )
    except Exception as identifier:
        print(points, half)



# def buildTree(points, height):
#     size = len(points)
#     half = size // 2
#     point = None if half == 0 else points[half]
#     result = Node(point)


#     if size == 1:
#         result.division = points[0]
#         result.left = None
#         result.right = None
#     elif height % 2 == 0:
#         tabx = sorted(points, key=lambda point: point.x)
#         result.division = tabx[half]

#         Lx = tabx[:half]
#         Rx = tabx[half + 1:]


#         result.left = buildTree(Lx, height + 1)
#         result.right = buildTree(Rx, height + 1)
#     else:
#         taby = sorted(points, key=lambda point: point.y)
        
#         result.division = taby[half]

#         Ly = taby[:half]
#         Ry = taby[half + 1:]



#         result.left = buildTree(Ly, height+1)
#         result.right = buildTree(Ry, height+1)

#     return result
