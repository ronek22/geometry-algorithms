import numpy as np
from point import Point

def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

def from_txt(filename):
    correct_data = []
    with open('data/' + filename, 'r') as f:
        data = [list(map(float, coord.strip().split(','))) for coord in f.readlines()]
    for coord in data:
        correct_data.append(Point(coord[0], coord[1]))
    return correct_data


def create_adj_matrix(filename='test1.txt', print=True):
    points = from_txt(filename)
    size = len(points)
    matrix = np.zeros((size,size))
    for x, point1 in enumerate(points):
        for y, point2 in enumerate(points):
            if(x == y): 
                matrix[x][y] = 0
            else:
                matrix[x][y] = point1.get_distance(point2)

    if print: matprint(matrix)
    return points, matrix

def get_edges_from_optimal_tour(tour):
    pass



