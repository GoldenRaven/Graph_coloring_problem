# Graphe coloring problem
This problem seems to be a very old problem, i don't get to know too much yet. This repository is my method to solve the problem, it's surely not a very good algorithm, any comments are encouraged.
## Some possible methods
These are some ideas i came to realize maybe possible to solve this problem, but may not be good enough to get a small color number.
### Color nodes from left to right one by one
### Color the node with max depth first, then the connected node with less depth. Keep doing this till all the nodes are colored.
### Grow method
0. The color number is determined by the max `closed` nodes. Define `closed`: several nodes, connected to each other, eg. triangle.
1. Find all `triangle` by searching the common nodes of given sides.
2. Grow all `tetrahedron` out of found `triangle` by searching common nodes of found triangles.
3. Keep growing until no common nodes found.
4. The number of nodes of `closed` graph in last step gives color number.
### Method of this repository
0. The color number is determined by the max closed nodes. Define `closed`: several nodes, connected to each other, eg. triangle.
