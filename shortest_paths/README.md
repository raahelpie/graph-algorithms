Modified BFS for unweighted graphs
--
Algorithm:
  - Maintain a distances array where the distance to every node is -1. Mark the distance to the source node to be 0.
  - Maintain a queue same as you would in normal BFS. Add the first source node to the queue.
  - While the queue is not empty, put out the node.
  - For each of the neighbors, if the distances[neightbor] is -1, meaning it has not been visited yet. Make the distances[neighbor] as distances[node] + 1 
  - Add this modified node to the queue
  - After the queue become empty, the distances array will have the shortest distances, if the value is -1, then that node cannot be visited from the selected source node.
  
 
General Structure for Shortest Path Algorithms
--

1. Initialisation:
    1. Initialize all distances to all the vertices as infinity
    2. Mark the previous node of all vertices as None
    3. Make the shortest distance to source as 0
   
2. Run a loop for edge (source, vertex) (somehow) until all edges are relaxed
3. Relax the vertices: \
    if d[v] > d[u] + edge_weight(u, v): d[v] = d[u] + edge_weight(u, v) and previous node of v is u
    
    
Dijkstra's Shortest Path Algorithm For Weighted Graphs
--
Algorithm:
  - Maintain a distances array where the distance to every node is positive infinity. Mark the distance to the source node to be 0.
  - Maintain a PriorityQueue of key-value pairs of (distance, node) pairs which tell you which node to visit next based on sorted minimum values.
  - Insert (0, source) into the priority queue (in the form of (distance[node], node)) as specified above.
  - While the PQ is not empty, put out the node with smallest distance (notice greedy here)
  - For all the neighboring edges of this node, relax each node - meaning check whether the current distance along with the edge between is lesser than the distances[to], if it is, update the distances array and add this new pair to PQ.
  - Mark the node as visited to avoid coming back to the same node again.
 
