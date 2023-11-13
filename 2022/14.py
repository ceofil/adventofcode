import sys
import numpy as np
from enum import Enum

class Cell(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2
    SOURCE = 3

paths = []
minx = np.inf  # no need for miny since source is at y=0 => miny will be 0 
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        path = []
        for coords in line.split('->'):
            x,y = map(int, coords.split(','))
            path.append((x,y))
            minx = min(minx, x)
        paths.append(path)

sourcex = 500 - minx
sourcey = 0
paths = [np.array(path) - np.array([minx,sourcey]) for path in paths]
maxx = max([np.max(path[:,0]) for path in paths])
maxy = max([np.max(path[:,1]) for path in paths])

grid = np.zeros((maxy+1,maxx+1), dtype=int)
for path in paths:
    for idx in range(len(path) - 1):
        x0, y0 = path[idx]
        x1, y1 = path[idx + 1]
        dx = 1 if x1 > x0 else -1
        dy = 1 if y1 > y0 else -1
        for mx in range(x0, x1 + dx, dx):
            for my in range(y0, y1 + dy, dy):
                grid[my, mx] = Cell.ROCK.value
# grid[sourcey, sourcex] = Cell.SOURCE.value   

grid = np.r_[grid, np.zeros((1, grid.shape[1]), dtype=int)]
grid = np.r_[grid, np.ones((1, grid.shape[1]), dtype=int) * Cell.ROCK.value]

vertical_extender = np.zeros((grid.shape[0], 1), dtype=int)
vertical_extender[-1] = Cell.ROCK.value
    

counter = 0
down = np.array([0, 1])
down_left = np.array([-1, 1])
down_right = np.array([1, 1])
moves = [down, down_left, down_right]
void_fall = False
while not void_fall:
    pos = np.array([sourcex, sourcey])
    if not grid[pos[1], pos[0]] == Cell.AIR.value:
        break
    rest = False
    while not (void_fall or rest):
        if pos[0] == 0:
            grid = np.c_[vertical_extender.copy(), grid]
            pos[0] = 1
            sourcex += 1
        if pos[0] == grid.shape[1] - 1:
            grid = np.c_[grid, vertical_extender.copy()]
        rest = True
        for move in moves:
            new_pos = pos + move
            nx, ny = new_pos
            if nx < 0:
                void_fall = True
                rest = False
                break
            if grid[new_pos[1], new_pos[0]] == Cell.AIR.value:
                pos = new_pos
                # print('next')
                rest = False
                break
    if rest:
        # print('rest')
        grid[pos[1],pos[0]] = Cell.SAND.value
        counter += 1
print(grid)
print(counter)