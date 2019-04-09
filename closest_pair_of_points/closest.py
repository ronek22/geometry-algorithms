import math
from matplotlib import pyplot as plt
import random

def draw(points, pt1, pt2):
    x, y = [x[0] for x in points], [x[1] for x in points]
    fig = plt.figure(1, figsize=(5,5), dpi=90)
    plt.scatter(x,y)
    plt.plot(*pt1, "or", color="g")
    plt.plot(*pt2, "or", color="g")

def solution(points):
    ax = sorted(points, key=lambda x: x[0]) # lista punktow sortowana po x
    ay = sorted(points, key=lambda x: (x[1],x[0])) # lista punktow sortowana po y
    p1, p2, mi = closest_pair(ax, ay)
    return p1, p2, mi

def closest_pair(ax, ay):
    size = len(ax)

    if size <= 3:
        return brute(ax)
        
    # dzielimy ax na dwie polowy
    mid = size // 2 
    Lx = ax[:mid]
    Rx = ax[mid:]

    midpoint = ax[mid][0]
    Ly = list()
    Ry = list()

    # Do ly wrzucamy dopoki nie osiagniemy midpointa z ax
    for x in ay:
        if x[0] < midpoint:
            Ly.append(x)
        else:
            Ry.append(x)

    (p_left, q_left, dist_left) = closest_pair(Lx, Ly)
    (p_right, q_right, dist_right) = closest_pair(Rx, Ry)

    # rekurencja zakonczona porownanie, wynikow z lewej i prawej
    if dist_left <= dist_right:
        dist = dist_left
        pair = (p_left,q_left)
    else:
        dist = dist_right
        pair = (p_right,q_right)

    # moze byc tak, ze jeden punkt znajduje sie po lewej stronie,
    # a drugi po prawej, i ich dystans moze byc mniejszy niz aktulany

    # sprawdz obszar w lewo i prawo od srodka 
    # oddalony o minimalny dystans dotychczasz znaleziony
    (p_split, q_split, dist_split) = closest_split_pair(ax, ay, dist, pair)

    if dist <= dist_split:
        return pair[0], pair[1], dist
    else:
        return p_split,q_split,dist_split

def brute(ax):
    mi = dist(ax[0], ax[1])
    best_pair = ax[0], ax[1]
    size = len(ax)

    if size == 2:
        return p1, p2, mi
    
    for i in range(size-1):
        for j in range(i+1, size):
            if i != 0 or j != 1:
                p, q = ax[i], ax[j]
                dst = dist(p, q)
                if dst < mi:
                    mi = dst
                    best_pair = ax[i], ax[j]
    return best_pair[0], best_pair[1], mi

def closest_split_pair(p_x, p_y, delta, best_pair):
    size_x = len(p_x)
    mx_x = p_x[size_x // 2][0] # wspolrzednia x srodka

    # wszystkie punkty, ktore mieszcza sie w pasie delta
    s_y = [x for x in p_y if x[0] <= abs(mx_x - delta)] 
    size_y = len(s_y)

    best = delta

    for i in range(size_y - 1):
        for j in range(i+1, min(i+7, size_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p,q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2)

def generate_test_case(length: int, _range: int):
    return list(set((random.randint(0, _range),random.randint(0, _range)) for i in range(length)))



if __name__ == "__main__":
    # test list
    # x = [1,2,3,3,-3,-1,2,1,-5]
    # y = [2,-1,-3,2,4,2,3,1,-2]

    points = generate_test_case(6, 20)

    point1, point2, distance = solution(points)
    draw(points, point1, point2)

    print(point1, point2, distance)

    plt.show()
