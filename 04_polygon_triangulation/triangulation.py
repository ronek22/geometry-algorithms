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
        self.vertices = sorted(vertices, key=lambda v: v.x)
    
    @classmethod
    def same_chain(cls, p1: Point, p2: Point):
        return p1.orientation == p2.orientation

    def triangulate(self):
        edges = []
        stack = [self.vertices[0], self.vertices[1]]
        
        for i, vi in enumerate(self.vertices[2:-1]):
            print("STACK: ", stack)
            print("FIRST ON STACK", stack[-1], " VERTEX: ", vi)
            # vi oraz wiercholek stosu sa na roznych lancuchach
            if not Triangulation.same_chain(vi, stack[-1]):
                print("DIFFERNT CHAINS")
                vk = stack[-1]
                while len(stack) != 0:
                    edges.append(Edge(vi, stack.pop(), color='y'))

                stack.append(vk)
                stack.append(vi)
            else:
                print("ON THE SAME CHAIN: ")
                vk = stack.pop()
                while len(stack) != 0:
                    vj = stack.pop()
                    print(vj, vk, vi)
                    if vj.turn_right(vk, vi):
                        edges.append(Edge(vi, vj, color='b'))
                    else:
                        break
                
                stack.append(vj)
                stack.append(vi)
        
        vn = self.vertices[-1]
        for i, item in enumerate(stack):
            if i not in [0, len(stack)]:
                edges.append(Edge(vn, item, color='g'))
        return edges

    def plot(self):
        '''
        plots graph of triangulation
        '''

        lines = self.triangulate()

        x_s, y_s = [point.x for point in self.unsorted_vertices], [point.y for point in self.unsorted_vertices]
        additional = 0
        while self.unsorted_vertices[0].x != x_s[-1]:
            point = self.unsorted_vertices[additional]
            x_s.append(point.x)
            y_s.append(point.y)
            additional += 1

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x_s, y_s, marker='o', linestyle='-', color='r', label='Points')

        for line in lines:
            ax.plot([line.p1.x, line.p2.x], [line.p1.y, line.p2.y], linestyle='-', color=line.color)

        # plt.show()