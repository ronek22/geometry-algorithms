import matplotlib.pyplot as plt

from point import Point
from edge import Edge
from polygon import Polygon
from utility import Utility

class Triangulation:
    
    def __init__(self, datafile='polygon.txt'):
        vertices = Utility().from_txt(datafile)
        self.polygon = Polygon(vertices)
        self.unsorted_vertices = vertices
        self.vertices = self.reorder(vertices)

    def reorder(self, vertices):
        sort_by_x, size = [], len(vertices)
        min_ix = vertices.index(min(vertices, key=lambda v: v.x))
        sort_by_x.append(vertices[min_ix])
        cw, ccw = (min_ix-1)%size, (min_ix+1)%size

        while len(sort_by_x) != size:
            if vertices[cw].x < vertices[ccw].x:
                sort_by_x.append(vertices[cw])
                cw = (cw-1)%size
            else:
                sort_by_x.append(vertices[ccw])
                ccw = (ccw+1)%size

        return sort_by_x
    
    @classmethod
    def same_chain(cls, p1: Point, p2: Point):
        return p1.orientation == p2.orientation

    def triangulate(self):
        self.plot_polygon()
        edges = []
        stack = [self.vertices[0], self.vertices[1]]
        
        for i, vi in enumerate(self.vertices[2:-1]):
            print("\tSTACK: ", stack)
            print("\tFIRST ON STACK", stack[-1], " VERTEX: ", vi)
            # vi oraz wiercholek stosu sa na roznych lancuchach
            if not Triangulation.same_chain(vi, stack[-1]):
                print("DIFFERNT CHAINS")
                vk = stack[-1]
                while len(stack) != 1:
                    edge = Edge(vi, stack.pop(), color='y')
                    edges.append(edge)
                    self.plot_diagonal(edge)
                stack.pop()

                stack.append(vk)
                stack.append(vi)
            else:
                print("ON THE SAME CHAIN: ")
                last_popped = None
                vk = stack.pop()
                while len(stack) != 0 and stack[-1].turn_right(vk, vi):
                    last_popped = stack.pop()
                    edge = Edge(vi, last_popped, color='b')
                    edges.append(edge)
                    self.plot_diagonal(edge)
                
                last_popped = vk if last_popped is None else last_popped
                stack.append(last_popped)
                stack.append(vi)
        
        print("STACK: ", stack)
        vn = self.vertices[-1]
        for i, item in enumerate(stack):
            if i not in [0, len(stack)-1]:
                edge = Edge(vn, item, color='g')
                edges.append(Edge(vn, item, color='g'))
                self.plot_diagonal(edge)
        return edges

    def plot_polygon(self):
        plt.ion()
        x_s, y_s = [point.x for point in self.unsorted_vertices], [point.y for point in self.unsorted_vertices]
        
        additional = 0
        while self.unsorted_vertices[0].x != x_s[-1]:
            point = self.unsorted_vertices[additional]
            x_s.append(point.x)
            y_s.append(point.y)
            additional += 1

        fig = plt.figure()
        self.ax = fig.add_subplot(111)
        self.ax.plot(x_s, y_s, marker='o', linestyle='-', color='r', label='Points')

        for point in self.unsorted_vertices:
            self.ax.plot(point.x, point.y, "or", color=point.color)
            self.ax.text(point.x, point.y, f"({point.x}, {point.y})")



    def plot_diagonal(self, line):
        self.ax.plot([line.p1.x, line.p2.x], [line.p1.y, line.p2.y], linestyle='-', color=line.color)
        plt.pause(0.1)
        plt.draw()

