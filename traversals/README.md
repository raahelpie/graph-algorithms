Comparing DFS and BFS
--------------------
The big advantage of DFS is that it has much lower memory requirements than BFS because
it's not required to store all the child nodes at each level. 

But depending upon the data we are looking for, either DFS or BFS can be advantageous.
Suppose if you are looking for someone in a family tree and you know that the person is still
alive, you are more likely to find him at the bottom of the tree, in such case DFS can be better.
BFS would take a long time for such searching. DFS would find it faster. And the other way
around, if you know that the person is dead long time back because the depth is likely to be
low, BFS would be a faster approach. 

Simply put, 
 - If solution is at lower depth: BFS
 - If solution is at maximum depth: DFS

Applications | DFS | BFS       
------- | ---------------- | ---------- 
Spanning forest, connected components, paths  | YES | YES
Shortest Paths  |         | YES
Minimal use of memory space   | YES | 