from node import Node
from area import Area

def searchArea(node: Node, area: Area):
    if node.is_leaf:
        checkLeaf(node, area)
    else:
        checkSubtree(node.left, area)
        checkSubtree(node.right, area)

def checkLeaf(node: Node, area: Area):
    if area.inside(node.data):
        reportOne(node.data)

def checkSubtree(node: Node, area: Area):
    if fullyContained(node.region, area):
        print("ZGLASZAM CALE PODDRZEWO")
        reportSubtree(node)
    elif intersects(node.region, area):
        searchArea(node, area)
    else:
        if node.is_leaf:
            checkLeaf(node, area)


def fullyContained(node: Area, area: Area):
    if node and area:
        if(node.bottomCorner[0] >= area.bottomCorner[0] and
            node.bottomCorner[1] >= area.bottomCorner[1] and
                node.topCorner[0] <= area.topCorner[0] and
                    node.topCorner[1] <= area.topCorner[1]):
            return True
    return False

def intersects(node: Area, area: Area):
    if node and area:
        # above or below
        if(area.topCorner[1] < node.bottomCorner[1] or
            area.bottomCorner[1] > node.topCorner[1]):
            return False
        # right or left doesnt interesect with region
        if(area.topCorner[0] < node.bottomCorner[0] or
            area.bottomCorner[0] > node.topCorner[0]):
            return False
    
        return True
    return False
        

def reportSubtree(node: Node):
    if node is None:
        return
    
    if node.is_leaf:
        print("\tZGLASZAM LISC: ", node.data)
        return
    
    if node.left:
        reportSubtree(node.left)

    if node.right:
        reportSubtree(node.right)


def reportOne(data: tuple):
    print("ZGLASZAM PUNKT", data)