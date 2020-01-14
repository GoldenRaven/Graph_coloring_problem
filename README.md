# Graphe coloring problem
This problem seems to be a very old problem, i don't get to know too much yet. This repository is my method to solve the problem, it's surely not a very good algorithm, any comments are encouraged.
## Some possible methods
These are some ideas i came to realize maybe possible to solve this problem, but may not be good enough to get a small color number.
### Color nodes from left to right one by one
### Color by node depth
the node with max depth first, then the connected node with less depth. Keep doing this till all the nodes are colored. See file color_by_depth.
### Grow method
The color number is determined by the max `closed` nodes. Define `closed`: several nodes, connected to each other, eg. triangle. Too much computations make this method impractical.
1. Find all `triangle` by searching the common nodes of given sides.
2. Grow all `tetrahedron` out of found `triangle` by searching common nodes of found triangles.
3. Keep growing until no common nodes found.
4. The number of nodes of `closed` graph in last step gives color number.
### Method of finding max closed graph
The color number is determined by the max closed nodes. Define `closed`: several nodes, connected to each other, eg. triangle. One more rule: the min color number of a colsed circle chain with even nodes is 2, but 3 for a closed chain with odd nodes.
1. Get the depth of every node. Get nodes that every node connected to, and restore them into `bonds`.
2. Count node depth, get the max possible color num.
3. For a color num, find common elements of every two lines in the 2D array `bonds`.
4. Check wether there is a `closed` graph of order `color_num` or higher or not.
4. If the repeated times of a common list is larger than color num, and the common list length longer than color num, then there is at least one `colsed` graph of order `color num`.
5. If exist, increase `color num`, repeat `step 3, 4, 5, 6`.
6. If not exist, decrease `color num` and  repeat `step 3, 4, 5, 6`.
7. If the difference between the successive `color num` is 1, exit the recycle.
8. The minimal color number is given by the last two `color num` accordingly.
