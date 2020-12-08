with open('aoc_3_1.txt') as f:
    wire_1 = f.readline().rstrip().split(",")
    wire_2 = f.readline().rstrip().split(",")

loc_1_x = [0]
loc_1_y = [0]
loc_2_x = 0
loc_2_y = 0
cross_x = []
cross_y = []
mindist = 595959595959

for i in wire_1:
    direction = i[0]
    steps = int(i[1:])
    for j in range(steps):
        if direction == 'R':
            loc_1_x.append(loc_1_x[-1]+1)
            loc_1_y.append(loc_1_y[-1])
        elif direction == 'L':
            loc_1_x.append(loc_1_x[-1]-1)
            loc_1_y.append(loc_1_y[-1])
        elif direction == 'U':
            loc_1_x.append(loc_1_x[-1])
            loc_1_y.append(loc_1_y[-1]+1)
        elif direction == 'D':
            loc_1_x.append(loc_1_x[-1])
            loc_1_y.append(loc_1_y[-1]-1)

for i in wire_2:
    direction = i[0]
    steps = int(i[1:])
    for j in range(steps):
        if direction == 'R':
            loc_2_x +=1
        elif direction == 'L':
            loc_2_x += -1
        elif direction == 'U':
            loc_2_y += 1
        elif direction == 'D':
            loc_2_y += -1

        for k in range(len(loc_1_x)):
            if (loc_2_x == loc_1_x[k]) & (loc_2_y == loc_1_y[k]):
                cross_x.append(loc_2_x)
                cross_y.append(loc_2_y)
                
for i in range(len(cross_x)):
    dist = abs(cross_x[i])+abs(cross_y[i])
    if dist < mindist:
        mindist = dist

print(mindist)
