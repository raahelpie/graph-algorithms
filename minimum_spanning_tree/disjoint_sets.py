size = {}
parent = {}
nodes = int(input())
for i in range(1, nodes+1):
    parent[i] = i                               # initially all nodes are parents to themselves
    size[i] = 1                                 # and the size of each set is 1 (the node itself)


def find(node):                                 # find function return ths root of the disjoint set
    x = node                                    # we make an alias for the node
    while x != parent[x]:                       # while the root is not itself
        x = parent[x]                           # we keep moving upwards
    while node != x:                            # after we have found the root, which is now "x"
        nex = parent[node]                      # we again start from node and store its parent in a varible
        parent[node] = x                        # we make the parent of all nodes in this set to root (compression)
        node = nex                              # run the loop by making the next node as the parent stored above
    return x


def union(a, b):                                # union is only done if both nodes belong to different sets
    r1 = find(a)                                # get the root of a
    r2 = find(b)                                # get the root of b
    if r1 == r2:                                # if they are both the same, return -1 (not joining the sets)
        return -1
    else:
        if size[r1] > size[r2]:                 # if they are not the same
            size[r1] += size[r2]                # add the smaller one to bigger one
            del size[r2]                        # delete the smaller one
            parent[r2] = r1                     # and make the parent of smaller one as bigger one
        else:
            size[r2] += size[r1]
            del size[r1]
            parent[r1] = r2
        return 1                                # return 1 saying that we are adding an edge
