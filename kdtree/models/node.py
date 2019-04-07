class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @property
    def is_leaf(self):
        return (not self.data) or (all(not bool(c) for c,p in self.children))

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

    
