from point import Point


def from_txt(filename='data.txt'):
    correct_data = []
    with open('data/' + filename, 'r') as f:
        data = [list(map(float, coord.strip().split(','))) for coord in f.readlines()]
    for coord in data:
        correct_data.append(Point(coord[0], coord[1]))
    return correct_data

