import sys
import numpy as np

data = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        numbers = map(lambda c: 1 if c == '@' else 0, line.strip())
        data.append(list(numbers))
data = np.array(data)

result = 0

removed = -1
while removed != 0:
    removed = 0
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            if data[y, x] == 0:
                continue
            nbh = data[
                max(0, y-1):min(data.shape[0], y+2), 
                max(0, x-1):min(data.shape[1], x+2)
            ].sum() - 1
            if nbh < 4:
                result += 1
                removed += 1
                data[y, x] = 0
    print("removed:", removed)
print("result:", result)
        
