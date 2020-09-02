from collections import deque

"""
The only difference this has with BFS is that in here, you have to pop the last element from the stack, instead of
popping the first element which would be the case in BFS
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


def depth_first_search_iterative(a_list):
    stack = deque()                                 # dfs uses a stack
    visited = set()                                 # visited set to avoid traversing the same node twice
    start = 1                                       # select any arbitrary node
    stack.append(start)                             # push into the stack
    while len(stack):                               # while the stack is not empty
        node = stack.pop()                          # perform pop operation (takes out the top element)
        print(node, end=" ")                        # print it out lmao
        visited.add(node)                           # add it to the visited set
        for neighbor in a_list[node]:               # for all the neighbors of the current node
            if neighbor not in visited:             # if it is not already visited
                stack.append(neighbor)              # push into the stack
    return


depth_first_search_iterative(adjacency_list)                # output: 1 4 7 3 2 6 8 5


def depth_first_search_recursive(a_list, node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in a_list[node]:
        if neighbor not in visited:
            depth_first_search_recursive(a_list, neighbor, visited)


visited = set()
depth_first_search_recursive(adjacency_list, 1, visited)

# TIME COMPLEXITY: O(V + E),  V is the number of vertices, and E is the number of edges
# SPACE COMPLEXITY: O(V + E), the general space required for the adjacency list and O(V) for the visited set
