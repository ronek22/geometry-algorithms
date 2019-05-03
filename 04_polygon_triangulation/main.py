from triangulation import Triangulation
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # monotonic = Triangulation(datafile='monotonic.txt')
    # monotonic.plot()

    # not_monotonic = Triangulation(datafile='not_monotonic.txt')
    # not_monotonic.plot()

    right = Triangulation(datafile='right.txt')
    right.plot()

    circle = Triangulation(datafile='circle.txt')
    circle.plot()
    
    plt.show()