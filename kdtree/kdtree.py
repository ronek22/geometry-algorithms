from models.node import Node
from functools import wraps
from collections import deque

def require_axis(f):
    """ Check if the object of the function has axis and sel_axis members """

    @wraps(f)
    def _wrapper(self, *args, **kwargs):
        if None in (self.axis, self.sel_axis):
            raise ValueError('%(func_name) requires the node %(node)s '
                    'to have an axis and a sel_axis function' %
                    dict(func_name=f.__name__, node=repr(self)))

        return f(self, *args, **kwargs)

    return _wrapper

class KDNode(Node):
    """Node contains kd-tree specific data and methods"""

    def __init__(self, data=None, left=None, right=None, axis=None, sel_axis=None, dimensions=None, division=None):
        super(KDNode, self).__init__(data, left, right)
        self.axis = axis
        self.sel_axis = sel_axis
        self.dimensions = dimensions
        self.division = division

    @require_axis
    def add(self, point):
        """
        Adds a point to the current node or iteratively
        descends to one of its children.
        Users should call add() only to the topmost tree.
        """

        current = self
        while True:
            check_dimensionality([point], dimensions=current.dimensions)

            # Adding has hit an empty leaf-node, add here
            if current.data is None:
                current.data = point
                return current

            # split on self.axis, recurse either left or right
            if point[current.axis] < current.data[current.axis]:
                if current.left is None:
                    current.left = current.create_subnode(point)
                    return current.left
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = current.create_subnode(point)
                    return current.right
                else:
                    current = current.right

    @require_axis
    def create_subnode(self, data):
        """ Creates a subnode for the current node """

        return self.__class__(data,
                axis=self.sel_axis(self.axis),
                sel_axis=self.sel_axis,
                dimensions=self.dimensions)


    @property
    def is_balanced(self):
        """ Returns True if the (sub)tree is balanced
        The tree is balanced if the heights of both subtrees differ at most by
        1 
        """

        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        if abs(left_height - right_height) > 1:
            return False

        return all(c.is_balanced for c, _ in self.children)


    def rebalance(self):
        """
        Returns the (possibly new) root of the rebalanced tree
        """

        return create([x.data for x in self.inorder()])


    def axis_dist(self, point, axis):
        """
        Squared distance at the given axis between
        the current Node and the given point
        """
        return math.pow(self.data[axis] - point[axis], 2)


    def dist(self, point):
        """
        Squared distance between the current Node
        and the given point
        """
        r = range(self.dimensions)
        return sum([self.axis_dist(point, i) for i in r])



def create(point_list=None, dimensions=None, axis=0, sel_axis=None):
    """ Creates a kd-tree from a list of points
    All points in the list must be of the same dimensionality.
    If no point_list is given, an empty tree is created. The number of
    dimensions has to be given instead.
    If both a point_list and dimensions are given, the numbers must agree.
    Axis is the axis on which the root-node should split.
    sel_axis(axis) is used when creating subnodes of a node. It receives the
    axis of the parent node and returns the axis of the child node. """

    if not point_list and not dimensions:
        raise ValueError('either point_list or dimensions must be provided')

    elif point_list:
        dimensions = check_dimensionality(point_list, dimensions)

    # by default cycle through the axis
    sel_axis = sel_axis or (lambda prev_axis: (prev_axis+1) % dimensions)

    if not point_list:
        return KDNode(sel_axis=sel_axis, axis=axis, dimensions=dimensions)

    # Sort point list and choose median as pivot element
    point_list = list(point_list)
    point_list.sort(key=lambda point: point[axis])
    median = len(point_list) // 2

    loc   = point_list[median]
    left  = create(point_list[:median], dimensions, sel_axis(axis))
    right = create(point_list[median + 1:], dimensions, sel_axis(axis))
    return KDNode(loc, left, right, axis=axis, sel_axis=sel_axis, dimensions=dimensions)


def check_dimensionality(point_list, dimensions=None):
    dimensions = dimensions or len(point_list[0])
    for p in point_list:
        if len(p) != dimensions:
            raise ValueError("All points must have the same dimension")

    return dimensions


def level_order(tree, include_all=False):
    """ Returns an iterator over the tree in level-order
    If include_all is set to True, empty parts of the tree are filled
    with dummy entries and the iterator becomes infinite. """

    q = deque()
    q.append(tree)
    while q:
        node = q.popleft()
        yield node

        if include_all or node.left:
            q.append(node.left or node.__class__())

        if include_all or node.right:
            q.append(node.right or node.__class__())



def visualize(tree, max_level=100, node_width=10, left_padding=5):
    """ Prints the tree to stdout """

    height = min(max_level, tree.height()-1)
    max_width = pow(2, height)

    per_level = 1
    in_level  = 0
    level     = 0

    for node in level_order(tree, include_all=True):

        if in_level == 0:
            print()
            print()
            print(' '*left_padding, end=' ')

        width = int(max_width*node_width/per_level)

        node_str = (str(node.data) if node else '').center(width)
        print(node_str, end=' ')

        in_level += 1

        if in_level == per_level:
            in_level   = 0
            per_level *= 2
            level     += 1

        if level > height:
            break

    print()
    print()


def findSplitNode(tree, x1, x2):
    v = tree
    while not v.is_leaf and (x2 <= v.data[0] or x1 > v.data[0]):
        if x2 <= v.data[0]:
            v = v.left
        else:
            v = v.right
    return v

def rangeQuery(tree, x_set, y_set):
    v = findSplitNode(tree, x_set[0], x_set[1])
    if v.is_leaf:
        print("POWININE BYC IMHO")
    else:
        pass




