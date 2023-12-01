import sys
import numpy as np
import re


data = []
unqiue_beacons_str = set()
# unqiue_beacons = []
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
        # beacon_str = f'{xb},{yb}'
        # unqiue_beacons.add(beacon_str)

line = 2_000_000 
if sys.argv[1].endswith('.test'):
    line = 10

n_positions = 0
already_subtracted_beacons = set()
for (xs, ys), (xb, yb) in data:
    manh_dist = np.abs(xb - xs) + np.abs(yb - ys)
    dy = np.abs(line - ys)
    if dy > manh_dist:
        continue
    horizontal_allowance = manh_dist - dy
    n_positions += horizontal_allowance * 2 
    beacon_str = f'{xb},{yb}'
    if beacon_str in already_subtracted_beacons:
        continue
    if yb == line and np.abs(xb - xs == horizontal_allowance):
        n_positions -= 1
        already_subtracted_beacons.add(beacon_str)
        
        
print(n_positions)