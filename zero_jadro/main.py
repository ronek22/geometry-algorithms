from matplotlib import pyplot as plt
from shapely.geometry.polygon import Polygon, orient
from shapely.geometry import mapping, shape
from utility import Utility
import json

util = Utility()


def from_json(filename='data.json'):
    with open(filename, 'r') as f:
        data = json.loads(f.read())
    return shape(data)

def find_min_max(polygon):
    #     _
    # /\ | | - kolec dolny; \/ |_| - kolec gorny

    coordinates = util.coords_as_list(polygon)
    for coord in coordinates:
        print(coord[0], coord[1])

    # only x 
    xaxis = list(zip(*coordinates))[0]
    for x in xaxis:
        print(x)


poly = Polygon([
    (0,0),
    (0,2),
    (1,1),
    (2,2),
    (2,0),
    (1,0.8),
])

triangle = from_json()

util.draw(*poly.exterior.xy)
util.draw(*triangle.exterior.xy)

find_min_max(triangle)

util.show()
