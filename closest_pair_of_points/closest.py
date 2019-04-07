import math
from matplotlib import pyplot as plt
import random

def draw(x, y, pt1, pt2):
    fig = plt.figure(1, figsize=(5,5), dpi=90)
    plt.scatter(x,y)
    plt.plot(*pt1, "or", color="g")
    plt.plot(*pt2, "or", color="g")

def solution(x, y):
    a = list(zip(x,y))
    ax = sorted(a, key=lambda x: x[0]) # lista punktow sortowana po x
    ay = sorted(a, key=lambda x: (x[1],x[0])) # lista punktow sortowana po y
    p1, p2, mi = closest_pair(ax, ay)
    return p1, p2, mi

def closest_pair(ax, ay):
    size = len(ax)

    if size <= 3:
        return brute(ax)
        
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

    (p1, q1, mi1) = closest_pair(Lx, Ly)
    (p2, q2, mi2) = closest_pair(Rx, Ry)

    if mi1 <= mi2:
        d = mi1
        mn = (p1,q1)
    else:
        d = mi2
        mn = (p2,q2)

    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3,q3,mi3

def brute(ax):
    mi = dist(ax[0], ax[1])
    p1, p2 = ax[0], ax[1]
    size = len(ax)

    if size == 2:
        return p1, p2, mi
    
    for i in range(size-1):
        for j in range(i+1, size):
            if i != 0 or j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1,p2,mi

def closest_split_pair(p_x, p_y, delta, best_pair):
    size_x = len(p_x)
    mx_x = p_x[size_x // 2][0] 

    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta
    size_y = len(s_y)

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
    x = [random.randint(0, _range) for i in range(length)]
    y = [random.randint(0, _range) for i in range(length)]
    return x,y



if __name__ == "__main__":
    # test list
    # x = [1,2,3,3,-3,-1,2,1,-5]
    # y = [2,-1,-3,2,4,2,3,1,-2]

    x, y = generate_test_case(30, 20)

    point1, point2, distance = solution(x,y)
    draw(x, y, point1, point2)

    print(point1, point2, distance)

    plt.show()
