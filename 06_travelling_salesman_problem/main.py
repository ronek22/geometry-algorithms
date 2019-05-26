from tsp import TSP
import numpy as np
from utility import create_adj_matrix
import argparse
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, 
        help='Give name of the file contains vertex\'s of cities data')
    args = parser.parse_args()
    name = args.file
    print(name)

    points, matrix = create_adj_matrix(filename=name)
    problem = TSP(matrix)
    problem.get_results()

    g = nx.from_numpy_matrix(matrix)
    nx.draw(g, [(point.x,point.y) for point in points], node_size=100)
    plt.axis('equal')
    plt.show()


