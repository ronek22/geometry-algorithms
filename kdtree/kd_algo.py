k = 2


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
        return {
            'point': points_x[n//2],
            'left': _buildTree(points_x[:n//2], points_y, depth + 1),
            'right': _buildTree(points_x[n//2 + 1:],points_y, depth+1)
        }
    else:
        return {
            'point': points_y[n//2],
            'left': _buildTree(points_x, points_y[:n//2], depth+1),
            'right': _buildTree(points_x, points_y[n//2 + 1:], depth+1)
        }

    

def buildTree(points, depth=0):
    n = len(points)

    if n <= 0:
        return None

    axis = depth % k

    sorted_points = sorted(points, key=lambda point: point[axis])

    return {
        'point': sorted_points[n // 2],
        'left': buildTree(sorted_points[:n // 2], depth + 1),
        'right': buildTree(sorted_points[n//2 + 1:], depth + 1)
}