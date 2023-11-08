import sys
import numpy as np
from queue import Queue
from tqdm import tqdm


with open(sys.argv[1], 'r') as fd:
    data = fd.read()


start_pos = None
end_pos = None
hmap = []
for y, line in enumerate(data.split('\n')):
    xS = line.find('S')
    if xS >= 0:
        start_pos = xS, y
        line = line.replace('S', 'a')
    xE = line.find('E')
    if xE >= 0:
        end_pos = xE, y
        line = line.replace('E', 'z')
    height = np.array(list(map(ord, line))) - ord('a')
    hmap.append(height)
    
    
end_pos = np.array(end_pos)
hmap = np.array(hmap, dtype=int)
    
path_lengths = []
start_positions = np.argwhere(hmap == 0)  # list of [y,x]
start_positions = start_positions[:, ::-1]  # making it a list of [x, y]
for start_pos in tqdm(start_positions):
    visited = np.zeros_like(hmap)
    next_to_visit = Queue()
    next_to_visit.put((start_pos.copy(), 0))
    possible_moves = np.array([
        [1,0],
        [-1,0],
        [0,1],
        [0,-1]
    ])
    goal_reached = False
    while not goal_reached:
        # print(f'{np.sum(visited)}/{(np.prod(visited.shape))}')
        if next_to_visit.empty():
            break
        agent, moves = next_to_visit.get()
        visited[agent[1], agent[0]] = 1
        for move in possible_moves:
            
            next_pos = agent + move
            if not 0 <= next_pos[1] < hmap.shape[0]:
                continue
            if not 0 <= next_pos[0] < hmap.shape[1]:
                continue
            if visited[next_pos[1], next_pos[0]]:
                continue
            if hmap[next_pos[1], next_pos[0]] - hmap[agent[1], agent[0]] > 1:
                continue
            visited[next_pos[1], next_pos[0]] = 1
            if all(end_pos == next_pos):
                path_lengths.append(moves + 1) 
                goal_reached = True
                break
            next_to_visit.put((next_pos, moves + 1))
print(min(path_lengths))
            
#34s