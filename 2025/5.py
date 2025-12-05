import sys
import numpy as np

data = []
with open(sys.argv[1], 'r') as file:
    str_ranges, str_ids = file.read().split('\n\n')
    ids = [int(l) for l in str_ids.splitlines()]
    ranges = []
    for l in str_ranges.splitlines():
        a, b = l.split('-')
        ranges.append((int(a), int(b)))
        
result = 0

ranges = sorted(ranges, key=lambda r: (r[0], r[1]))

prev_max = -1
for r in ranges:
    left = max(r[0], prev_max + 1)
    right = r[1]
    if left > right:
        continue
    delta = right - left + 1
    print(r, left, right, delta)
    result += delta
    prev_max = max(right,prev_max)
    
print(ranges)
print("result:", result)  
