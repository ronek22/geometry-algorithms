from area import Area

class Node:
    def __init__(self, split=None, data=None, left=None, right=None, axis=None, region: Area=None):
        """data should be k dimension tuple """
        self.split = split        
        self.data = data
        self.left = left
        self.right = right
        self.axis = axis
        self.region = None
        self.parent = None
        if left:
            left.parent = self
        if right:
            right.parent = self

    @property
    def is_left(self):
        return self == self.parent.left

    @property 
    def is_right(self):
        return self == self.parent.right

    @property
    def get_axis(self):
        return 'x' if self.axis == 0 else 'y'

    @property
    def is_leaf(self):
        return not(self.left or self.right)

    def inorder(self):

        if not self:
            return

        if self.left:
            for x in self.left.inorder():
                yield x

        yield self

        if self.right:
            for x in self.right.inorder():
                yield x

    @property
    def children(self):
        """ 
        Returns iterator for children, return as (Node, pos) where
        pos = 0 for the left subnode and pos = 1 for the right.
        """

        if self.left and self.left.axis is not None:
            yield self.left, 0
        if self.right and self.right.axis is not None:
            yield self.right, 1

    def height(self):
        min_height = int(bool(self))
        return max([min_height] + [c.height()+1 for c, p in self.children])

    
    def __bool__(self):
        return self.axis is not None

    

    # def __repr__(self):
    #     return '<%(cls)s - %(data)s>' % \
    #     dict(cls=self.__class__.__name__, data=repr(self.is_leaf) + "\t" + repr(self.data) + "\t" + repr(self.region) if self.data else repr(self.split)+"\t" + repr(self.region))

    def __repr__(self):
        return repr(self.data) if self.data else repr(self.region) + "\t" + repr(self.get_axis)