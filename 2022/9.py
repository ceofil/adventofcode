import sys
import numpy as np

string_to_dir = {
    'R': np.array([1, 0]),    
    'L': np.array([-1, 0]),    
    'D': np.array([0, 1]),    
    'U': np.array([0, -1])    
}

unique_position = set()

start = np.array([0, 0])

rope = np.zeros((10, 2))
unique_position.add(str(rope[0]))

with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        dir_string, n_string = line.split(' ')
        n = int(n_string)
        dir = string_to_dir[dir_string]
        
        for _ in range(n):
            rope[-1] += dir
            for idx in range(rope.shape[0] - 2, -1, -1):
                # print(idx)
                diff = rope[idx + 1] - rope[idx]
                if np.max(np.abs(diff)) <= 1:
                    continue
                curr_dirr = np.clip(diff, -1, 1)
                rope[idx] += curr_dirr 
            unique_position.add(str(rope[0]))
        # print(line.rstrip('\n')) 
        
print(f'result = {len(unique_position)}')