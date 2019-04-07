"""
Basically just start at the root node and use mins and maxes to check if the two child nodes are inside the rectangle. 
Then recurse down to the leaf nodes and check if the points in the leaves are inside the rectangle.
"""

from models.node import Node
from models.area import Area
from models.point import Point
k = 2



    

def buildTree(points, depth=0):
    n = len(points)

    if n <= 0:
        return None

    axis = depth % k

    sorted_points = sorted(points, key=lambda point: point[axis])

    return Node(sorted_points[n//2], 
        buildTree(sorted_points[:n//2], depth+1),
        buildTree(sorted_points[n//2+1:], depth+1),
        axis
    )


def rangeSearch(root: Node, area: Area):
    if root.is_leaf:
        if area.is_inside(root.data):
            return root.data
        else:
            return None
    if area.is_inside(root.left.data):
        rangeSearch(root.left, area)
    if area.is_inside(root.right.data):
        rangeSearch(root.left, area)

def searchArea(node: Node, area: Area):
    result = []
    temp = []

    if node.is_leaf:
        print("LISC:", node.data)
        if area.is_inside(node.data):
            result.append(node.data)
            print("RESULT: ", result)
    if node.left is not None:
        temp = searchArea(node.left, area)
        result.extend(temp)
    if node.right is not None:
        temp = searchArea(node.right, area)
        result.extend(temp)

    return result

"""
tuple function build_kd_tree(int depth, set points):
    if points contains only one point:
        return that point as a leaf.

    if depth is even:
        Calculate the median x-value.
        Create a set of points (pointsLeft) that have x-values less than
            the median.
        Create a set of points (pointsRight) that have x-values greater
            than or equal to the median.
    else:
        Calculate the median y-value.
        Create a set of points (pointsLeft) that have y-values less than
            the median.
        Create a set of points (pointsRight) that have y-values greater
            than or equal to the median.

    treeLeft = build_kd_tree(depth + 1, pointsLeft)
    treeRight = build_kd_tree(depth + 1, pointsRight)

    return(median, treeLeft, treeRight)
"""

"""
# DOESNT WORK
def createTree(points):
    ax = sorted(points, key=lambda x: x[0])
    ay = sorted(points, key=lambda x: x[1])
    

    return _buildTree(ax, ay)


def _buildTree(points_x, points_y, depth=0):

    axis = depth % k
    n = len(points_x) if axis == 0 else len(points_y)

    if n <= 0:
        return None

    if axis == 0:
        return Node(points_x[n//2],
             _buildTree(points_x[:n//2], points_x[:n//2], depth + 1),
            _buildTree(points_x[n//2 + 1:],points_x[n//2 + 1:], depth+1)
        )
    else:
        return Node(points_y[n//2],
            _buildTree(points_y[:n//2], points_y[:n//2], depth+1),
            _buildTree(points_y[n//2 + 1:], points_y[n//2 + 1:], depth+1)
        )
"""