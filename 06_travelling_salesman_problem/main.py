from tsp import TSP
import numpy as np

if __name__ == "__main__":
    distances = np.full((6,6), 10000)
    distances[5][0] = 10
    distances[1][5] = 12
    distances[4][1] = 2
    distances[2][4] = 4
    distances[3][2] = 6
    distances[0][3] = 8

    print(distances)

    problem = TSP(distances)
    problem.get_results()