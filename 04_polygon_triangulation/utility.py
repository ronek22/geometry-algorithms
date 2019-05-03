from matplotlib import pyplot as plt
import json
from polygon import Polygon
from point import Point

class _Utility:
    _instance = None
    
    def __init__(self):
        self._fig_counter = 0

    @property
    def fig_number(self):
        return self._fig_counter

    def draw(self, x, y):
        self._fig_counter += 1
        fig = plt.figure(self._fig_counter, figsize=(5,5), dpi=90)
        ax = fig.add_subplot(111)
        ax.plot(x, y, alpha=0.7, linewidth=3)
        ax.scatter(x,y)
        ax.set_title('Polygon')

    def draw_spikes(self, polygon):
        fig = plt.figure(self._fig_counter)
        ax = fig.get_axes()[0]
        topx, topy = polygon.topSpike.get_xy
        bottx, botty = polygon.bottomSpike.get_xy
        ax.plot(topx, topy, "or", color='r')
        ax.plot(bottx, botty, "or", color='g')

    def redraw(self, x, y, _color):
        fig = plt.figure(self._fig_counter)
        ax = fig.get_axes()
        ax[0].plot(x,y,"or", color=_color)

    def from_txt(self, filename='data.txt'):
        self._fig_counter += 1
        correct_data = []
        with open('data/' + filename, 'r') as f:
            data = [list(map(int,coord.strip().split(' '))) for coord in f.readlines()]
        for coord in data:
            correct_data.append(Point(coord[0], coord[1]))
        return correct_data

    def show(self):
        plt.show()

def Utility():
    if _Utility._instance is None:
        _Utility._instance = _Utility()
    return _Utility._instance


