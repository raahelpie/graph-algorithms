# Irrespective of directed or undirected. In an unweighted graph, all the edges are of the same weight, we consider 1.
# This is modified BFS where instead of using the visited set, we use an array of hashmap to use it as both:
# to determine a vertex has been visited before
# to denote the how far the vertex is from the selected source

from collections import deque
adjacency_list = {
    'A': ['B', 'D'],
    'B': ['D', 'E'],
    'C': ['A', 'F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': [],
    'G': 'F'
}

n = 7
distances = {}
for each in adjacency_list:
    distances[each] = -1                                            # intialize all values to -1

source = 'A'                                                        # select the source from which you want distances
distances[source] = 0                                               # 0 is the shortest distance from node to itself
queue = deque()
queue.append(source)
while len(queue):                                                   # while q is not empty
    node = queue.popleft()                                          # take the first element out
    for neighbour in adjacency_list[node]:                          # for each of its neighbours
        if distances[neighbour] == -1:                              # if it is unvisited
            queue.append(neighbour)                                 # add it to the queue
            distances[neighbour] = distances[node] + 1              # and make its distance one more than the source's


print(distances)  # {'A': 0, 'B': 1, 'C': -1, 'D': 1, 'E': 2, 'F': 2, 'G': 2}  -1 denotes C cannot be visited from src
