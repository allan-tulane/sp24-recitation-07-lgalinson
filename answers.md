# CMPS 2200 Recitation 10## Answers

**Name:** Lakeland Galinson
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work is $W(2m) + W(n) + O(1)$

- **4)**
In the worst case, we select a starting node and call reachable once. This function traverses the entire graph. If it reaches every node, the graph is connected. Reachable is called only once in all cases.

- **5)**
The work is $W(2m) + W(n) +O(1)$

- **7)**
Switching from an adjacency list to an adjacency matrix changes the `reachable` function's complexity from $O(n + m)$ to $O(n^2)$ because you must check all potential connections for each node, making it less efficient for sparse graphs.


