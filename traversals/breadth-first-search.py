from collections import deque

"""
Usually graphs are represented using adjacency lists
In Python, we do the same - using dictionaries where:
key - node (an integer denoting the node)
value - neighboring list (a list of nodes it has an edge with/towards)


Note that if the graph has more than one component, you need to run a loop from 1-N and for every node, if it is not
visited, then call the BFS function on it. The visited set should be the same for both the main function and the bfs 


You can also do the traversal using a simple python list, but it does not provide O(1) tc of popleft() which deque does
"""

# Below is an adjacency list of an undirected graph
adjacency_list = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1],
    4: [1, 7],
    5: [2],
    6: [2, 8],
    7: [4],
    8: [6]
}


def breadth_first_search(a_list):
    queue = deque()                                 # bfs uses a queue
    visited = set()                                 # visited set to avoid traversing the same node twice
    start = 1                                       # select any arbitrary node
    queue.append(start)                             # add it to the queue and to the visited
    while len(queue):                               # while the queue is not empty
        node = queue.popleft()                      # take the first element out
        print(node, end=" ")                        # print it out lmao
        visited.add(node)                           # add it to the visited set
        for neighbor in adjacency_list[node]:       # for all the neighbors of the current node
            if neighbor not in visited:             # if it is not already visited
                queue.append(neighbor)              # add it to the end of the queue
    return


breadth_first_search(adjacency_list)                # output: 1 2 3 4 5 6 7 8

# TIME COMPLEXITY: O(V + E),  V is the number of vertices, and E is the number of edges
# SPACE COMPLEXITY: O(V + E), the general space required for the adjacency list and O(V) for the visited set
