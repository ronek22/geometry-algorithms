from utility import Utility
from polygon import Polygon
from point import Point

util = Utility()


# Wczytywanie z pliku
polytxt = util.from_txt('data4.txt')

util.draw(*polytxt.get_axes())
print("Istnieje jądro? ", polytxt.check_kernel())
util.draw_spikes(polytxt)

# =======================================
polygon = Polygon([
    Point(3,1), Point(4,3), Point(5,1),
    Point(6,3), Point(6,5), Point(6,6),
    Point(5,5), Point(4,5), Point(2,6),
    Point(1,5), Point(2,3), 
])

util.draw(*polygon.get_axes())
print("Istnieje jądro? ", polygon.check_kernel())
util.draw_spikes(polygon)

util.show()
