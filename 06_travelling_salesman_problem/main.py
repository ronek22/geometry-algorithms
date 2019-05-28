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
    optimal_tour = problem.get_results()


    g = nx.from_numpy_matrix(matrix)
    nx.draw_networkx(g, [(point.x,point.y) for point in points], nodelist=list(range(len(points))),node_size=200, node_color='g')
    nx.draw_networkx_edges(g,[(point.x,point.y) for point in points],
                       edgelist=optimal_tour,
                       width=4,alpha=0.8,edge_color='r')
    plt.axis('equal')
    plt.show()


