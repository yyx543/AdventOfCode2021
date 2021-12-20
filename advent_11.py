import sys
sys.setrecursionlimit(9999999)

str_inp = '''6617113584
6544218638
5457331488
1135675587
1221353216
1811124378
1387864368
4427637262
6778645486
3682146745'''

temp1 = str_inp.split("\n")

lst = []
zeros = []
for line in temp1:
    temp2 = []
    zero_temp = []
    for i in line:
        temp2.append(int(i))
    zeros.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    lst.append(temp2)

def increase_neighbours(grid, x, y):
    for i in range(max(0,x-1), min(x+2, 10)):
        for j in range(max(0,y-1), min(y+2, 10)):
            if i == x and j == y:
                continue
            else:
                grid[i][j] += 1
                if grid[i][j] == 10:
                    grid = increase_neighbours(grid, i, j)
    return grid

count = 0
i = 1
while True:
    for x in range(10):
        for y in range(10):
            lst[x][y] += 1
            if lst[x][y] == 10:
                lst = increase_neighbours(lst, x, y)
    for x in range(10):
        for y in range(10):
            if lst[x][y] > 9:
                lst[x][y] = 0
                if i < 101:
                    count += 1
    if lst == zeros:
        break
    i += 1
            
print(f"Part 1: {count}")
print(f"Part 2: {i}")