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
    if line[0] not in neighbour_dict[line[1]] and line[0] != "start":
        neighbour_dict[line[1]].append(line[0])
    if line[1] not in neighbour_dict[line[0]] and line[1] != "start":
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
    neighbours = get_neighbours(node)
    visited.append(node)

    if node == "end":
        paths.append(copy.deepcopy(visited))
    else:
        for neighbour in neighbours:
            if neighbour.isupper():
                visiting1(neighbour, copy.deepcopy(visited))
            elif neighbour not in visited:
                visiting1(neighbour, copy.deepcopy(visited))


start_node = "start"
paths = []
visiting1("start", [])
print(f"Part 1: {len(paths)}")


def visiting2(node, visited, duplicate):
    neighbours = get_neighbours(node)
    visited.append(node)

    if node == "end":
        paths.append("".join(visited))
    else:
        for neighbour in neighbours:
            if neighbour.isupper() or neighbour not in visited:
                visiting2(neighbour, copy.deepcopy(visited), duplicate)
            elif not duplicate:
                visiting2(neighbour, copy.deepcopy(visited), True)

paths = []
visiting2("start", [], False)
print(f"Part 2: {len(paths)}")