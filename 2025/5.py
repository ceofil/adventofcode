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
for i in ids:
    for r in ranges:
        if r[0] <= i <= r[1]:
            result += 1
            break
print("result:", result)
