from build import buildTree, set_regions
from search import searchArea
from area import Area
from utility import draw, visualize


if __name__ == "__main__":
    x = [1,2,3,5,4,9,8,7,6] 
    y = [2,5,9,1,3,8,6,4,7]

    # x = [4,2,1]
    # y = [3,5,2]

    points = list(zip(x,y))

    kdtree = buildTree(points)
    area = Area([0,3], [5,10])
    kdtree.region = Area([min(x),min(y)], [max(x),max(y)])
    kdtree.region = Area([0,0], [10,10])
    
    set_regions(kdtree)
    searchArea(kdtree, area)

    # print("HEIGHT: ", kdtree.height())

    print(kdtree.get_axis)

    for node in kdtree.inorder():
        print(node)
    # visualize(kdtree)

    draw(x, y, area, kdtree)
    print("KONIEC")