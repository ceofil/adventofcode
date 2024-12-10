import numpy as np
from tqdm import tqdm

with open("inputs/6", "r") as fd:
    map = fd.readlines()
    map = [list(row.replace("\n", "")) for row in map]

dir = np.array([0, -1])
pos = None

for y, row in enumerate(map):
    if pos is not None:
        break
    for x, cell in enumerate(row):
        if cell == '^':
            pos = np.array([x, y])
            break

assert pos is not None, "^ not found"
startingPos = pos.copy()
startingDir = dir.copy()

def rotateDir(dir):
    return np.array([-dir[1], dir[0]])

def inside(pos):
    return 0 <= pos[0] < len(map[0]) and 0 <= pos[1] < len(map)

def getBlock(pos):
    return map[pos[1]][pos[0]]

def run(startingPos, startingDir):
    global map
    pos = startingPos.copy()
    dir = startingDir.copy()
    visited = set((pos[0], pos[1], dir[0], dir[1]))
    infLoop = False
    while inside(pos):
        tup = (pos[0], pos[1], dir[0], dir[1])
        if tup in visited:
            infLoop = True
            break
        else:
            visited.add(tup)
        nextPos = pos + dir

        if not inside(nextPos):
            break
        if getBlock(nextPos) == "#":
            dir = rotateDir(dir)
        else:
            pos = nextPos
    return infLoop

    
res = 0
for y in tqdm(list(range(0, len(map)))):
    for x in range(0, len(map[0])):
        o = np.array([x,y])
        if getBlock(o) != ".":
            continue
        map[o[1]][o[0]] = "#"

        infLoop = run(startingPos, startingDir)
        if infLoop:
            res += 1
        map[o[1]][o[0]] = "."

print(res)