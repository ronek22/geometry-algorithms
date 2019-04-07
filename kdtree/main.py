from kdtree import visualize, create
import kd_algo
from kdsearch import Point, buildTree
from models.area import Area
import json
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


def draw(x,y, area, tree):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    rect = plt.Rectangle(area.bottomCorner, area.width, area.height, color='k', alpha=0.3)

    ax.add_patch(rect)
    ax.scatter(x,y)

    for node in tree.inorder():
        if node.get_axis == 'y':
            plt.axhline(y=node.data[1], color='b', linestyle='-', linewidth=.2)
        else:
            plt.axvline(x=node.data[0], color='b', linestyle='-', linewidth=.2)



if __name__ == "__main__":
    x = [4,2,1]
    y = [3,5,2]

    x = [1,2,3,5,4,7,8,7,6] 
    y = [2,5,9,1,3,9,6,4,7]

    points = list(zip(x,y))
    area = Area(Point(3,2), Point(5,4))

    print(points)

    sorting_every = kd_algo.buildTree(points)

    areaResult = kd_algo.searchArea(sorting_every, area)

    print(areaResult)

    visualize(sorting_every)
    draw(x, y, area, sorting_every)

    plt.show()


    