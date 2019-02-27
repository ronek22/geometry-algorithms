from matplotlib import pyplot as plt
from shapely.geometry.polygon import Polygon
from utility import Utility

util = Utility()

poly = Polygon([
    (0,0),
    (0,2),
    (1,1),
    (2,2),
    (2,0),
    (1,0.8),
])

triangle = Polygon([
    (0,0),
    (0,3),
    (4,0)
])


util.draw(*poly.exterior.xy)
util.draw(*triangle.exterior.xy)

print(util.coords_as_list(poly))
util.show()
