from collections import deque

adjacency_list = {
    0: [2, 3, 6],
    1: [4],
    2: [6],
    3: [1, 4],
    4: [5, 8],
    5: [],
    6: [7, 11],
    7: [4, 12],
    8: [],
    9: [2, 10],
    10: [6],
    11: [12],
    12: [8],
    13: []
}

n = 13

indegree = [0 for i in range(n+1)]                      # initialize the indegree of all nodes to zero

for node in adjacency_list:                             # for each node in the graph
    for neighbor in adjacency_list[node]:               # go through all its neighbours
        indegree[neighbor] += 1                         # and increment the neighbours indegree

queue = deque()                                         # just a queue

for i in range(n+1):                                    # loop over all the nodes
    if indegree[i] == 0:                                # and if the indegree of it is 0
        queue.append(i)                                 # add it to the queue


topological_ordering = []

count = 0                                               # counts the number of nodes added to the top sort array
while len(queue):                                       # while the queue is not empty
    node = queue.popleft()                              # take a node out
    topological_ordering.append(node)                   # add it to the topological sort array
    count += 1
    for neighbor in adjacency_list[node]:               # for each of its neighbours
        indegree[neighbor] -= 1                         # decrement the indegree (as we take the node out of the graph)
        if indegree[neighbor] == 0:                     # if its indegree turns out to be 0
            queue.append(neighbor)                      # add it to the queue
if count == n+1:                                        # [0, 9, 13, 3, 2, 10, 1, 6, 7, 11, 4, 12, 5, 8]
    print(topological_ordering)
else:                                                   # if all nodes are not added, then we have a loop
    print("Oops! There is a loop")
