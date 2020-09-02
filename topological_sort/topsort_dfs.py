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

"""
Algorithm:
1. Go through nodes from 0/1-N
2. If the node is not already visited, perform DFS on it
3. In the DFS, as you backtrack, add the node to the top_sort array in the beginning
4. Do this until all nodes are added to the top_sort array
"""

visited = set()

stack = deque()



def dfs(node):
    visited.add(node)
    for each in adjacency_list[node]:
        if each not in visited:
            dfs(each)
    stack.appendleft(node)


for i in range(n+1):
    if i not in visited:
        dfs(i)


for each in stack:
    print(each, end=" ")           # 13 9 10 0 3 1 2 6 11 7 12 4 8 5

