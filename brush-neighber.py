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
# pop the first element of bond
# for i in  range(node_num):
    # bond[i].pop(0)
# print(bond)
# print("")
#depth of node
depth = [len(bond[i])-1 for i in range(node_num)]
# print(depth)
# print("")
#count depth num, (depth, num of depth)
max_depth = max(depth)
count_depth = [(i, depth.count(i)) for i in range(max_depth+1)]
# print(max_depth)
# print(count_depth)
# print("")
#(depth, num of nodes whose depth >= depth)
acumulate_depth = [(j, len([i for i in depth if i >= j])) for j in range(max_depth+1)]
# print(acumulate_depth)
#possible closed graph, color num = possible_counts + 1
possible_counts = [acumulate_depth[i][0] for i in range(len(acumulate_depth)) if acumulate_depth[i][0] < acumulate_depth[i][1]]
# print(possible_counts)
possible_counts.reverse()
# print(possible_counts)
# print("")
#descending order, half-divide
color_num_up = possible_counts[0] + 1
if side_num != 0:
    color_num_down = 2
else:
    color_num_down = 1
color_num = int((color_num_up+color_num_down)/2)
print("color num start with ", color_num)
# print(color_num_up,color_num_down,color_num)
while 1:
    #pick node whose depth >= color_num -1
    candidate = [bond[i] for i in range(len(bond)) if depth[i] >= color_num-1]
    # print("")
    #pick those showing time >= color_num, restore their index
    index = []
    for i in range(len(candidate)):
        # print(candidate[i])
        count = sum([x.count(candidate[i][0]) for x in candidate])
        if count >= color_num:
            index.append(i)
    # print("")
    # print("fdsafs")
    # print(index)
    if len(index) >= color_num:
        # check whether closed or not?
        # print("pick ", color_num, "nodes in ", len(index), " nodes")
        # print("")
        # for i in index:
            # print(candidate[i])
        # candidate.pop(1)
        # print("")
        # for i in range(len(candidate)):
        #     print(candidate[i])
        # print("xxx")
        #get common list of candidate
        commons = []
        for i in range(len(candidate)):
            for j in range(i+1, len(candidate)):
                common = list(set(candidate[i]) & set(candidate[j]))
                if len(common) >= color_num :
                    commons.append(common)
        # print(commons)
        #count repeat times in commons, if count >= color_num, exist!
        # commons_count = []
        exist =  0
        for i in range(len(commons)):
            count = 0
            for j in range(len(commons)):
                if list(set(commons[i]) & set(commons[j])) == commons[i]:
                    count = count + 1
            # pailie = cn2
            comb_num = comb(color_num, 2)
            if count >= comb_num:
                print(commons[i], " appear ", count, " times")
                exist = 1
                break
            # commons_count.append(count-1)
        # print(commons_count)
        # exit(0)
        if exist:
            color_num_down = color_num
            if color_num_up - color_num <= 3:
                color_num = color_num + 1
            else:
                color_num = int((color_num+color_num_up)/2)
            continue
    print("up limit = ", color_num_up, " down limit = ",color_num_down , " color num = ", color_num)
    #terminate condition
    if color_num - color_num_down == 1 :
        color_num = color_num_down
        print("color num = ", color_num)
        exit(0)
    print("???")
    color_num_up = color_num
    if color_num - color_num_down <= 3:
        color_num = color_num - 1
    else:
        color_num = int((color_num+color_num_dwon)/2)
    exit(0)
exit(0)
for i in range(max_depth):
    # print(possible_counts[i][0])
    print(possible_counts[i][1])
# print(possible_counts)

#find common node of side
for side in range(side_num):
    tmp = [i for i in bond[int(grow[side][0])] if i in bond[int(grow[side][1])]]
    grow[side].extend(tmp)
side_grow = [len(grow[i]) for i in [j for j in range(len(grow))]]

#get the index of sides having a triangle form
count = 0
index = []
for i in side_grow:
    if i > 2:
        index.append(count)
    count = count + 1

#erase sides having only two nodes connected
grow = [grow[i] for i in index]
# print(grow)
# print(len(grow))

#erase repeated configeration
for i in range(len(grow)):
    for j in range(len(grow)):
        # print(i,j,a[i],a[j])
        if sorted(grow[i]) == sorted(grow[j]) and  j > i:
            # print(i,j,a[i],a[j])
            grow[j] = ''
grow = [i for i in grow if i]
a = [[1, 2, 3], [1, 3, 2], [1, 3, 4], [2, 1, 4], [1, 2, 3]]
print(a.count(3))

print(len(grow))


print(grow)


# print(data[20][:])
