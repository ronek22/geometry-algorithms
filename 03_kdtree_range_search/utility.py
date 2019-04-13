from area import Area
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import collections as mc
from collections import deque

def draw(x,y, area, tree):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    rect = plt.Rectangle(area.bottomCorner, area.width, area.height, color='k', alpha=0.3)

    ax.add_patch(rect)
    ax.scatter(x,y)

    for node in tree.inorder():
        if not node.is_leaf:
            line_bottom_x = [node.region.pmin[0], node.region.pmax[0]]
            line_bottom_y = [node.region.pmin[1], node.region.pmin[1]]
            line_left_x = [node.region.pmin[0], node.region.pmin[0]]
            line_left_y = [node.region.pmin[1], node.region.pmax[1]]
            line_right_x = [node.region.pmax[0], node.region.pmax[0]]
            line_right_y = [node.region.pmin[1], node.region.pmax[1]]
            line_top_x = [node.region.pmin[0], node.region.pmax[0]]
            line_top_y = [node.region.pmax[1], node.region.pmax[1]]

            ax.plot(line_left_x, line_left_y, color='g', linewidth=.3)
            ax.plot(line_top_x, line_top_y, color='b', linewidth=.3)
            ax.plot(line_bottom_x, line_bottom_y, color='b', linewidth=.3)
            ax.plot(line_right_x, line_right_y, color='g', linewidth=.3)

    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

    plt.show()


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
    in_level = 0
    level = 0

    for node in level_order(tree, include_all=True):

        if in_level == 0:
            print()
            print()
            print(' '*left_padding, end=' ')

        width = int(max_width*node_width/per_level)

        if node:
            if node.data:
                node_str = (str(node.data)).center(width)
            else:
                node_str = (str(node.region)).center(width)


        print(node_str, end=' ')

        in_level += 1

        if in_level == per_level:
            in_level = 0
            per_level *= 2
            level += 1

        if level > height:
            break

    print()
    print()