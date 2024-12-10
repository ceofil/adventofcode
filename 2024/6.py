import numpy as np



with open("inputs/6", "r") as fd:
    map = fd.readlines()
    map = [row.replace("\n", "") for row in map]


pos = None
found = False

for y, row in enumerate(map):
    if found:
        break
    for x, cell in enumerate(row):
        if cell == '^':
            pos = np.array([x, y])
            found = True
            break

assert found, "^ not found"


def printMap():
    print('\n'.join(map))


dir = np.array([0, -1])
def rotateDir(dir):
    return np.array([
        -dir[1],
        dir[0]
    ])

def inside(pos):
    return 0 <= pos[0] < len(map[0]) and 0 <= pos[1] < len(map)

def getBlock(pos):
    return map[pos[1]][pos[0]]


visited = set()

def visit(pos):
    print(pos)
    visited.add((pos[0], pos[1]))

visit(pos)
while inside(pos):
    visit(pos)
    nextPos = pos + dir
    if not inside(nextPos):
        break
    if getBlock(nextPos) == "#":
        dir = rotateDir(dir)
    else:
        pos = nextPos

printMap()
print(len(visited))