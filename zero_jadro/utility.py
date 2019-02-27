from matplotlib import pyplot as plt

class _Utility:
    _instance = None
    
    def __init__(self):
        self._fig_counter = 0

    def draw(self, x, y):
        self._fig_counter += 1
        fig = plt.figure(self._fig_counter, figsize=(5,5), dpi=90)
        ax = fig.add_subplot(111)
        ax.plot(x, y, alpha=0.7, linewidth=3, solid_capstyle='round')
        ax.set_title('Polygon')

    def coords_as_list(self, polygon):
        return list(zip(*polygon.exterior.coords.xy))

    def show(self):
        plt.show()

def Utility():
    if _Utility._instance is None:
        _Utility._instance = _Utility()
    return _Utility._instance


