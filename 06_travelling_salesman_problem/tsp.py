import numpy as np
import itertools
from math import inf

# * Time Complexity: O(n^2 * 2^n)
# * Space Complexity: O(n * 2^n)

class TSP:
    def __init__(self, distances, start=0, solved=False):
        if distances.ndim != 2: raise ValueError("Array must be 2d")
        if distances.shape[0] != distances.shape[1]: raise ValueError("Array must be square")

        self.distances = distances
        self.start = start
        self.solved = solved
        self.minTourCost = inf
        self.optimalTour = []

    def get_results(self):
        if not self.solved: self.solve()
        print("~"*60)
        print("Optimal tour: ", *self.optimalTour, sep="->")
        print(f"Minimal cost of tour: {self.minTourCost}")

    def solve(self):
        N = self.distances.shape[0]
        start = self.start
        END_STATE = (1 << N) - 1
        memo = np.full((N, 1 << N), 0)
        
        for end in range(N):
            if end==start: continue
            memo[end][(1 << start) | (1 << end)] = self.distances[start][end]

        
        # for r in range(3, N+1): # r - number of nodes in partly completed tour
        #     for subset in self.combinations(r, N): # loop all subsets
        #         if self.notInBinSeq(start, subset): continue # we need to make sure a start node is in subset, otherwise we couldn't make valid tour
        #         for next_node in range(N):
        #             if next_node==start or self.notInBinSeq(next_node, subset): continue
        #             subset_without_next = subset ^ (1 << next_node)
        #             minDist = inf # positive infinity, try to minimisie for the next node
        #             for end in range(N):
        #                 if end == start or end == next_node or self.notInBinSeq(end, subset): continue
        #                 newDist = memo[end][subset_without_next] + self.distances[end][next_node]
        #                 minDist = min(minDist, newDist)
        #             memo[next_node][subset] = minDist

        for r in range(3, N+1): # r - number of nodes in partly completed tour
            subsets = (subset for subset in self.combinations(r, N) if self.inSet(start, subset)) # generator for looping all subsets, that have start node inside
            for subset in subsets:
                for next_node in range(N):
                    if next_node != start and self.inSet(next_node, subset):
                        subset_without_next, minDist = subset ^ (1 << next_node), inf
                        for end_node in range(N):
                            if end_node != start and end_node != next_node and self.inSet(end_node, subset): 
                                newDist = memo[end_node][subset_without_next] + self.distances[end_node][next_node]
                                minDist = min(minDist, newDist)
                        memo[next_node][subset] = minDist


        for i in range(N):
            if i == start: continue
            tourCost = memo[i][END_STATE] + self.distances[i][start]
            self.minTourCost = min(tourCost, self.minTourCost)

        lastIndex = start
        state = END_STATE
        self.optimalTour.append(start)

        for i in range(1, N):
            index = -1
            for j in range(N):
                if j==start or self.notInBinSeq(j, state): continue
                if index == -1: index = j
                prevDist = memo[index][state] + self.distances[index][lastIndex]
                newDist = memo[j][state] + self.distances[j][lastIndex]
                if newDist < prevDist: index=j
            self.optimalTour.append(index)
            state = state ^ (1 << index)
            lastIndex = index
        
        self.optimalTour.append(start)
        self.solved = True
        self.optimalTour = self.optimalTour[::-1]


    # TODO: Check how it works...
    def notInBinSeq(self, elem, subset):
        return (1 << elem) & subset == 0

    def inSet(self, elem, subset):
        return (1 << elem) & subset != 0

    def combinations(self, r, n, debug=False):
        """Generate all binary combinations of length n with r bits set"""
        powers = [1 << e for e in range(n)]
        result = {sum(bits) for bits in itertools.combinations(powers, r)}
        if debug: 
            bit_format = "{0:0" + str(n) + "b}"
            print(*map(bit_format.format, result), sep="\n")
        return result
            
        


