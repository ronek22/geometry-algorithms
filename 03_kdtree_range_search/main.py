from build import createTree, set_regions
from search import searchArea
from area import Area
from utility import draw, visualize


if __name__ == "__main__":
    x = [1,2,3,5,4,9,8,7,6] 
    y = [2,5,9,1,3,8,6,4,7]


    points = list(zip(x,y))
    kdtree = createTree(points)
    
    area = Area([5,3.5], [10,10])
    kdtree.region = Area([min(x),min(y)], [max(x),max(y)])
    kdtree.region = Area([0,0], [10,10])
    
    set_regions(kdtree)
    searchArea(kdtree, area)

    # for node in kdtree.inorder():
    #     print(node)
    # visualize(kdtree)

    draw(x, y, area, kdtree)
    print("KONIEC")