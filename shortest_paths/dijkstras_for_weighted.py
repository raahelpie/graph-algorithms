from collections import defaultdict
from queue import PriorityQueue

"""
For weighted graphs, we store the vertices and edges in the following format:
from: [(to, weight), (to, weight), (to, weight)]
"""
adjacency_list = {
    1: [(2, 4), (3, 1)],
    2: [(5, 4)],
    3: [(4, 4), (2, 2)],
    4: [(5, 4)],
    5: []
}
n = 5
distances = [float("inf") for i in range(n+1)]              # initialize all distances to infinity
source = 1                                                  # select your source
distances[source] = 0                                       # shortest distance from a node to itself is zero

q = PriorityQueue()                                         # Consider a priority queue which sorts on basis of dists
q.put((distances[source], source))                          # hence, put in format of (distance, node)
visited = set()                                             # to avoid visiting same node twice

while q.qsize():                                            # while the queue is not empty
    currentDistance, node = q.get()                         # take the currentDist and node out (pop)
    if node not in visited:
        for each in adjacency_list[node]:                   # for all its neighbours
            to, dist = each
            if distances[to] > currentDistance + dist:      # see if sum of current distance and the
                distances[to] = currentDistance + dist      # weight of edge between is less than the currentdistance
                q.put((distances[to], to))                  # of to, if it is, change it and add it to the queue
        visited.add(node)                                   # mark our node as visited

for i in range(2, n+1):
    print(f"Shortest path from 1 to {i} is {distances[i]}")
