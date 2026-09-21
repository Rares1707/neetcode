Here are the NeetCode problems that I solved.

Below are notes for the problems.


# Trees

- depth-of-binary-tree
    - BFS / DFS / Iterative DFS
    - you needed help with the Iterative DFS; treat it like you are also using a global variable instead of simulating the usual DFS and also put the 'state' (depth of current node) in the stack in a bottom-up approach (no need to use the second half of the recursion)

- binary-tree-diameter
    - DFS / Iterative DFS
    - for the iterative DFS you need to store the heights in a dict and simulate both the forward and the backward passes of the recursion by doing this:
        - when arriving at a node, if it is not visited, put on the stack: the node itself (marked as visited this time) and its children (marked as unvisited)