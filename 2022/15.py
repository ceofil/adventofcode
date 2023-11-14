import sys
import numpy as np
import re


data = []
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        matches = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
        assert len(matches) == 2
        xs, ys = map(int, matches[0])
        xb, yb = map(int, matches[1])
        data.append([
            [xs,ys],
            [xb,yb]
        ])



line = 2_000_000

positions = set()

for (xs, ys), (xb, yb) in data:
    manh_dist = np.abs(xb - xs) + np.abs(yb - ys)
    dy = np.abs(line - ys)
    if dy > manh_dist:
        continue
    horizontal_allowance = manh_dist - dy
    for mx in range(xs-horizontal_allowance, xs + horizontal_allowance + 1):
        positions.add(mx)
        
for (_, _), (xb, yb) in data:
    if yb == line:
        if xb in positions:
            positions.remove(xb)
print(len(positions))