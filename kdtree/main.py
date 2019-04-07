import kdtree
import kd_algo
from kdsearch import Point, buildTree
import json

if __name__ == "__main__":
    x = [4,2,1]
    y = [3,5,2]
    # thirdtree = buildTree(points2, 0)

    # x = [1,2,3,5,4,7,8,7,6] 
    # y = [2,5,9,1,3,9,6,4,7]

    points = list(zip(x,y))
    print(points)

    # tree = kdtree.create(points)
    # kdtree.visualize(tree)
    # print(kdtree.findSplitNode(tree, 6, 8))
    kdtree = kd_algo.createTree(points)
    second = kd_algo.buildTree(points)

    serialized_tree = json.dumps(kdtree, indent=4)
    serialized_second= json.dumps(second, indent=4)
    

    print(serialized_tree)
    print(serialized_second)
    # print(second)

    