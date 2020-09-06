size = {}
parent = {}


def find(node):  # find function return ths root of the disjoint set
    x = node  # we make an alias for the node
    while x != parent[x]:  # while the root is not itself
        x = parent[x]  # we keep moving upwards
    while node != x:  # after we have found the root, which is now "x"
        nex = parent[node]  # we again start from node and store its parent in a varible
        parent[node] = x  # we make the parent of all nodes in this set to root (compression)
        node = nex  # run the loop by making the next node as the parent stored above
    return x


def union(a, b):  # union is only done if both nodes belong to different sets
    r1 = find(a)  # get the root of a
    r2 = find(b)  # get the root of b
    if r1 == r2:  # if they are both the same, return -1 (not joining the sets)
        return -1
    else:
        if size[r1] > size[r2]:  # if they are not the same
            size[r1] += size[r2]  # add the smaller one to bigger one
            del size[r2]  # delete the smaller one
            parent[r2] = r1  # and make the parent of smaller one as bigger one
        else:
            size[r2] += size[r1]
            del size[r1]
            parent[r1] = r2
        return 1  # return 1 saying that we are adding an edge


"""
Kruskal's algorithm:

1. Sort all the edges
2. Loop through these edges one by one starting from the smallest
3. Examine the two nodes connected to this edge, check if they belong to different sets
4. If the both nodes belong to the same set, it means adding this edge will create a cycle, so don't add
5. If they belong to different sets, add this edge and perform an union of those sets
6. MST is a tree, so the number of edges should be one less than number of nodes
7. If you add n-1 edges, then you can stop the above process
"""

n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b, weight = map(int, input().split())
    edges.append([weight, [a, b]])

edges.sort(key=lambda x:x[0])

for i in range(1, n + 1):
    parent[i] = i  # initially all nodes are parents to themselves
    size[i] = 1  # and the size of each set is 1 (the node itself)


def kruskals(n, edges):
    cost = 0
    for each in edges:
        print(f"Looking at edge of weight {each[0]} between {each[1][0]} and {each[1][1]}")
        if n-1:
            if union(each[1][0], each[1][1]) == 1:      # if we add an edge
                n -= 1                                  # decrease edges to be added yet
                cost += each[0]                         # add the weight of the current edge to the total cost
        else:
            break
    print(cost)


kruskals(n, edges)

"""
10 18
1 2 5
2 3 4
1 4 4
1 5 1
4 5 2
2 4 2
5 6 1
6 7 7
4 6 5
4 7 11
4 8 2
7 8 1
3 8 4
8 9 6
7 9 4
3 9 1
3 10 2
9 10 0




14
"""