import sys
import numpy as np

with open(sys.argv[1], 'r') as file:
    lines = file.read().splitlines()
pos = lines[0].index('S')

beams = np.zeros(len(lines[0]), dtype=int)
beams[pos] = 1

for line in lines[1:]:
    splitter = np.array([1 if c == '^' else 0 for c in line], dtype=int)
    intersection = np.prod([beams, splitter], axis=0).clip(0, 1)
    split_idexes = np.where(intersection)[0]
    new_beams = np.copy(beams)
    new_beams[split_idexes - 1] += new_beams[split_idexes]
    new_beams[split_idexes + 1] += new_beams[split_idexes]
    new_beams[np.where(splitter == 1)[0]] = 0
    beams = np.copy(new_beams)


print("result:", sum(beams))
