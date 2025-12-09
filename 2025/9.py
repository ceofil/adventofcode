import sys
import numpy as np
from tqdm import tqdm

data = []
with open(sys.argv[1], 'r') as fd:
    for line in fd:
        numbers = map(float, line.strip().split(','))
        data.append(np.array(list(numbers)))


def compute_area_of_rectangle(p1, p2):
    lengths = np.abs(p1 - p2) + 1
    return np.prod(lengths)

max_area = 0
for i1, p1 in tqdm(enumerate(data), total=len(data)):
    for i2, p2 in enumerate(data[:i1]):
        area = compute_area_of_rectangle(p1, p2)
        if area > max_area:
            max_area = area
print("result:", max_area)