from triangulation import Triangulation
import matplotlib.pyplot as plt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='right.txt', 
        help='Give name of the file contains vertex\'s polygon data')
    args = parser.parse_args()
    filename = args.file

    polygon = Triangulation(datafile=filename)
    polygon.triangulate()

    input("Press any key to end")