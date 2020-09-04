from collections import defaultdict
from queue import PriorityQueue
from collections import deque

"""
For weighted graphs, we store the vertices and edges in the following format:
from: [(to, weight), (to, weight), (to, weight)]
"""
"""
Shortest path problems involving graphs with weights have a optimal substructure,
meaning to get a destination V, and to find the optimal path to V, we could first find the optimal path to the vertices
before V and then decide which vertex to choose based on their edge weights. So, similar to how in the famous coin change
problem, to find the minimum coins to make a change of X, you consider all denominations and find the minimum coins
to (X-a, X-b, X-c) and then again for each one of them, you store it in a hashmap. Dijkstra's does the same but also
follows a greedy approach (using priority queue) to get to the time complexity of O(VlogV + E)  

Algorithm:

1. Initializing: This is done in all shortest path algorithms, you initialize the distance to all vertices as inifite
                 You make the distance to the source as zero

2. Now you add the source node to the priority queue and every vertex from this node, you tell them - the path cost
   to reach you, if you come through me is: 'The best you could get to me and the edge weight we have between us'
   Right? So, for the source node the best you could do the source node itself is 0.
   So, for all the reachable nodes from source nodes, you say to them, if someone wants to get to you through me (src),
   it is 0 + weight(src, neighbor). Note to say this is the shortest, but certainly the shortest if getting to it
   through source node. The best to the neighbours are now 'relaxed' as they have come down from infinity to presentvals
   
3. Because now, we have a better answer to the neighbours, maybe their neighbours can be relaxed to better values,
   So, to process them, you add every relaxed vertex to the priority queue.
   
4. You continue to do this till all nodes are relaxed and there are no more nodes to process.

Notice how in graphs involving negative cycles, the relaxataion never stops, you continue to find a better value
to a certain node either involved in the negative cycle or is directly connected to it. Hence, the queue never gets 
empty and the while loop runs infinitely.

This is why dijskra's doesn't work in graphs with negative edge weights.

Reason to use priority queue:

1. In a graph, say - the source node is directly connected to nodes A and B.
2. In the first step, we relax both nodes A and B and add them to the PQ
3. As source node is now processed we add it to the proccessed set. 
4. Suppose now, the edge A has a better path through B. But if you start processing A, and relax all its neighbours,
   and then come to process B and find out that A has a better path, you again add it to the queue and you will have to
   process A again and all the work it has done till now (relaxing A's edges is a waste of time).
5. Another thing is that, if you dont use a priority queue, after processing a certain node you cannot say for sure that
   the best path to that node is now certain and can be added to the proccessed set (for the same reason above, you can
   find a better path through B, maybe?)
6. Using a PQ has two advantages:
    1. We don't waste time processing a node to which there could potentially be a better path (bcoz PQ will make sure
       to choose the node with lesser currentDistance), meaning that if you are processing a certain node, you can be 
       sure that the best to it has become certain.
    2. After you process a certain node, you can add it to a set and if this node is a neighbor for any other node,
       you dont have to consider this node to relax now (as its best has already become certain)    

"""
adjacency_list = {
    1: [(2, 4), (3, 1)],
    2: [(5, 4)],
    3: [(4, 4), (2, 2)],
    4: [(5, 4)],
    5: []
}
n = 5
distances = [float("inf") for _ in range(n+1)]              # initialize all distances to infinity
source = 1                                                  # select your source
distances[source] = 0                                       # shortest distance from a node to itself is zero

q = PriorityQueue()                                         # Consider a priority queue which sorts on basis of dists
q.put((distances[source], source))                          # hence, put in format of (distance, node)
processed = set()                                             # to avoid visiting same node twice
prev = [None for i in range(n+1)]
while q.qsize():                                            # while the queue is not empty
    currentDistance, node = q.get()                         # take the currentDist and node out (pop)
    if node not in processed:
        for each in adjacency_list[node]:                   # for all its neighbours
            to, dist = each
            if to not in processed:
                if distances[to] > currentDistance + dist:      # see if sum of current distance and the
                    prev[to] = node
                    distances[to] = currentDistance + dist      # weight of edge between is < than the currentdistance
                    q.put((distances[to], to))                  # of to, if it is, change it and add it to the queue
        processed.add(node)                                       # mark our node as visited


def shortestpath(end):
    path = deque()
    if distances[end] == float("inf"):
        return path
    at = end
    while at:
        path.appendleft(at)
        at = prev[at]
    return path


"""
Explanation of the shortestpath function:

You see how, in line 32, we specified prev[to] = node, think of why we are doing so.
This happens whenever we are relaxing, and the idea of relaxation is that we are saying:hey,
we have found a better path than what exists at the moment, and the path we followed to getting there is (node)->(to)

The best would could do till node along with the edge weight, happens to be lesser than what was stored,
so naturally the path we would follow to get to 'to', it would include node as the last node of the path (before 'to')

And of course, as we relax multiple times, we keep changing it to a better node through which the shortest path comes.
And as we do it for every node, we know for a fact that every node has previous node to it in its shortest path.
So, what we do is, pass the vertex to which we want to get the actual path (sequence of vertices to follow),
We ask for what is the previous node to this current node and we put it in the array
Now, we change the current node to the value inserted (because now we want the previous node of the previous vertix)
We go through a loop, and we get to the first source point to which the previous node would be null, and hence the
loop stops and we will have the shortest path. (Note that, as we come from destination to source, the way we insert
elements matters, so if you just append to the end, you will have the path from destination to source, reverse it or 
append to the beginning using a deque as I did in the function above). 
"""

for i in range(2, n+1):
    print(f"Shortest path from 1 to {i} is {distances[i]}")
    print(f"Path is {shortestpath(i)}")
print(prev)