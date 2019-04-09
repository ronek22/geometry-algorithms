from node import Node
from copy import deepcopy


def createTree(points):
    points_x = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])
    points = [points_x, points_y]

    return buildTree(points)

def getMedian(points, axis, n):
    half = n // 2

    if n%2 == 0:
        return (points[half][axis] + points[half-1][axis])/2
    else:
        return points[half][axis]

def split(points, median, axis, n):
    left, right = [], []
    
    for i in range(0, n):
        value = points[i][axis]
        if value <= median:
            left.append(points[i])
        else:
            right.append(points[i])
    return left, right


def buildTree(points, depth=0):
    n = len(points[0])
    axis = depth % 2

    if n == 1:
        return Node(data=points[axis][0], axis=depth)
    elif n == 0:
        return None

    median = getMedian(points[axis], axis, n)

    leftX, rightX = split(points[0], median, axis, n)
    leftY, rightY = split(points[1], median, axis, n)

    left = [leftX, leftY]
    right = [rightX, rightY]
    # help_printer(depth, left, right, axis)

    vleft = buildTree(left, depth+1)
    vright = buildTree(right, depth+1)
    return Node(split=median, data=None, left=vleft, right=vright, axis=axis)


def set_regions(node: Node):
    if not node.is_leaf:
        if node.parent:
            # print("___ L:", node.is_left, ", ___ R:", node.is_right)
            parent = node.parent
            split = parent.split
            node.region = parent.region
            region = deepcopy(node.region)  # temp

            if None not in (region, split):
                if node.get_axis == 'y':
                    if node.is_left:
                        region.pmax[0] = split
                    else:
                        region.pmin[0] = split
                else:
                    if node.is_left:
                        region.pmax[1] = split
                    else:
                        region.pmin[1]= split
                node.region = region

        if node.left:
            set_regions(node.left)
        if node.right:
            set_regions(node.right)


def help_printer(depth, left, right, axis):
    if axis == 0:
        print("d= ", depth, " LEFT LIST:\n", left)
        print("d= ", depth, " RIGHT LIST:\n", right)
    else:
        print("d= ", depth, " TOP LIST:\n", left)
        print("d= ", depth, " BOTTOM LIST:\n", right)