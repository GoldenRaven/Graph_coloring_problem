import numpy as np
from scipy.special import comb
data = np.loadtxt("input")
data = data.astype(int)

node_num = data[0][0]
side_num = data[0][1]

grow = data[1:][:].tolist()

#space for bond
bond = [[j for i in range(1)] for j in range(node_num)]
#count bond into bond
for node in range(node_num):
    for line_num in range(side_num):
        if grow[line_num][0] == node:
            bond[node].append(grow[line_num][1])
        elif grow[line_num][1] == node:
            bond[node].append(grow[line_num][0])
# for i in range(len(bond)):
#     print(bond[i])
#depth of node
depth = [len(bond[i])-1 for i in range(node_num)]
#count depth num, (depth, num of depth)
max_depth = max(depth)
count_depth = [(i, depth.count(i)) for i in range(max_depth+1)]
#(depth, num of nodes whose depth >= depth)
acumulate_depth = [(j, len([i for i in depth if i >= j])) for j in range(max_depth+1)]
# print(acumulate_depth)
#possible closed graph, color num = possible_counts + 1
possible_counts = [acumulate_depth[i][0] for i in range(len(acumulate_depth)) if acumulate_depth[i][0] < acumulate_depth[i][1]]
possible_counts.reverse()
color_num_up = possible_counts[0] + 1
# print(color_num_up)
if side_num != 0:
    color_num_down = 2
else:
    color_num_down = 1
if color_num_up == color_num_down:
    color_num = color_num_down
    print("min color num = ", color_num_down)
    exit(0)
#descending order, half-divide
color_num = int((color_num_up+color_num_down)/2)
print("color num start with ", color_num)
# print(color_num_up,color_num_down,color_num)
while 1:
    print("up limit = ", color_num_up, " down limit = ",color_num_down , " testing ", color_num)
    #pick node whose depth >= color_num -1
    candidate = [bond[i] for i in range(len(bond)) if depth[i] >= color_num-1]
    # for i in range(len(candidate)):
    #     print(candidate[i])
    #pick those showing time >= color_num, restore their index
    index = []
    for i in range(len(candidate)):
        count = sum([x.count(candidate[i][0]) for x in candidate])
        # print([x.count(candidate[i][0]) for x in candidate])
        if count >= color_num:
            index.append(i)
    # print(index)
    if len(index) >= color_num:
        # check whether closed or not?
        # print("pick ", color_num, "nodes in ", len(index), " nodes")
        #get common list of candidate
        commons = []
        for i in range(len(candidate)):
            for j in range(i+1, len(candidate)):
                common = list(set(candidate[i]) & set(candidate[j]))
                if len(common) >= color_num :
                    commons.append(common)
        # for i in range(len(commons)):
            # print(commons[i])
        #count repeat times in commons
        # count_commons = []
        closed =  0
        # print(len(commons))
        for i in range(len(commons)):
            count = 0
            for j in range(len(commons)):
                if list(set(commons[i]) & set(commons[j])) == commons[i]:
                    count = count + 1
            # count_commons.append(count)
            # print(count)
            comb_num = comb(color_num, 2)
            if count >= comb_num:#if count >= comb_num, closed!
            # if count >= color_num:
                max_closed = commons[i]
                times = count
                # print(max_closed, " appear ", times, " times")
                closed = 1
                # print(count, comb_num)
                break
        if closed:
            color_num_down = color_num
            if color_num_up - color_num_down <= 3:
                color_num = color_num_down + 1
            else:
                color_num = int((color_num_down+color_num_up)/2)
            continue
    #terminate condition
    if color_num - color_num_down == 1 :
        color_num = color_num_down
        if color_num == 2:
            toend = 1
            #check whether the chain can be fill by two colors
            chain = []
            chain.append(0)#first node filled with color 0
            chain.append(1)#second node filled with color 0
            for i in range(2,node_num):
                position = i
                left_bond = [x for x in bond[i] if x < i]
                left_color = [chain[x] for x in left_bond]
                if len(left_color) == 0:
                    color = 0
                elif left_color.count(left_color[0]) == len(left_color):
                    if left_color[0] == 0:
                        color = 1
                    elif left_color[0] == 1:
                        color = 0
                else:
                    # print("not to end, position = ", position)
                    toend = 0
                    break
                chain.append(color)
            if not toend :
                color_num_down = 3#odd number of node head to tail connected
                color_num = color_num_down
                # print("not toend")
            else:
                print("chain: ", chain)
        #print minimum color number
        print("min color num = ", color_num)
        # for i in range(len(commons)):
            # print(commons[i])
        # print(count_commons)
        # print(max_closed, " appear ", times, " times")
        exit(0)
    color_num_up = color_num
    if color_num - color_num_down <= 3:
        color_num = color_num - 1
    else:
        color_num = int((color_num+color_num_down)/2)
