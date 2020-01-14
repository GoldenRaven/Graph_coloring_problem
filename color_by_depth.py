import numpy as np
from scipy.special import comb

# a = [1, 3, 4, 5]
# b = [1, 3, 4, 5]
# print(len(list(set(a) - set(b))))
# exit(0)

data = np.loadtxt("input")
data = data.astype(int)

node_num = data[0][0]
side_num = data[0][1]

side = data[1:][:].tolist()

#space for bond
bond = [[j for i in range(1)] for j in range(node_num)]
#count bond into bond
for node in range(node_num):
    for line_num in range(side_num):
        if side[line_num][0] == node:
            bond[node].append(side[line_num][1])
        elif side[line_num][1] == node:
            bond[node].append(side[line_num][0])
# for i in range(len(bond)):
    # print(bond[i])
#depth of node
depth = [(bond[i][0], len(bond[i])-1) for i in range(node_num)]
#restore colors
color = {}
colored_node = []
for i in range(len(depth)):
    for j in range(i ,len(depth)):
        if depth[i][1] < depth[j][1] :
            tmp = depth[i]
            depth[i] = depth[j]
            depth[j] = tmp
# print(depth)
next_node = depth[0][0]
#paint node
color[next_node] = 0
colored_node.append(next_node)
#start the loop to paint nodes
while 1:
    node = bond[next_node]
    # print("")
    # print(next_node, node)
    colored_bond = list(set(node) & set(colored_node))
    # print(node, colored_node)
    bad_color = [color[i] for i in colored_bond]
    # print(bad_color)
    uncolored_bond = list(set(node) - set(colored_bond))
    if len(uncolored_bond) == 0 :
        uncolored_node = list(set(list(range(node_num))) - set(colored_node))
        depth = [(i, len(bond[i])-1) for i in uncolored_node]
    else:
        depth = [(i, len(bond[i])-1) for i in uncolored_bond]
    for i in range(len(depth)):
        for j in range(i ,len(depth)):
            if depth[i][1] < depth[j][1] :
                tmp = depth[i]
                depth[i] = depth[j]
                depth[j] = tmp
    # print(depth)
    next_node = depth[0][0]
    for c_i in range(node_num):
        # print(c_i)
        if c_i not in bad_color:
            # print(color)
            # print(c_i, bad_color)
            color[next_node] = c_i
            break
    colored_node.append(next_node)
    if len(color) == node_num :
        color_nodeorder = [color[x] for x in sorted(color.keys())]
        print(max(color_nodeorder)+1)
        print(color_nodeorder)
        exit(0)
