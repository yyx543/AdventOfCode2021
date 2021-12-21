from typing import DefaultDict, OrderedDict
import sys
import copy

sys.setrecursionlimit(99999)


inp_str = '''pq-GX
GX-ah
mj-PI
ey-start
end-PI
YV-mj
ah-iw
te-GX
te-mj
ZM-iw
te-PI
ah-ZM
ey-te
ZM-end
end-mj
te-iw
te-vc
PI-pq
PI-start
pq-ey
PI-iw
ah-ey
pq-iw
pq-start
mj-GX'''

inp_lst = inp_str.split("\n")

neighbour_dict = DefaultDict(list)

for line in inp_lst:
    line = line.split("-")
    neighbour_dict[line[1]].append(line[0])
    neighbour_dict[line[0]].append(line[1])

def get_neighbours(node):
    return neighbour_dict[node]

def check_occurences(path, node):
    count = 0
    for i in path:
        if i == node:
            count += 1
    return count

def visiting1(node, visited):
    visited.append(node)
    if node == "end":
        paths.append(copy.deepcopy(visited))
    else:
        neighbours = get_neighbours(node)
        for neighbour in neighbours:
            if neighbour.isupper() or neighbour not in visited:
                visiting1(neighbour, copy.deepcopy(visited))

def visiting2(node, visited, duplicate):
    visited.append(node)
    if node == "end":
        paths.append("".join(visited))
    else:
        neighbours = get_neighbours(node)
        for neighbour in neighbours:
            if neighbour == "start":
                continue
            elif neighbour.isupper() or neighbour not in visited:
                visiting2(neighbour, copy.deepcopy(visited), duplicate)
            elif not duplicate:
                visiting2(neighbour, copy.deepcopy(visited), True)

start_node = "start"
paths = []
visiting1(start_node, [])
print(f"Part 1: {len(paths)}")
paths = []
visiting2(start_node, [], False)
print(f"Part 2: {len(paths)}")