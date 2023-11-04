import numpy as np
import sys


with open(sys.argv[1], 'r') as fd:
    rows = []
    for line in fd.readlines():
        row = []
        for digit in line.rstrip('\n'):
            row.append(int(digit))
        rows.append(row)
    
rows = np.array(rows)
# print(rows)



def naive(matrix):
    assert matrix.shape[0] == matrix.shape[1]
    size = matrix.shape[0]
    best_score = 0
    for y in range(1, size - 1):
        for x in range(1, size - 1):
            value = matrix[y, x]
            
            left =   matrix[y, :x]
            right =  matrix[y,  x+1:]
            top =    matrix[:y, x] 
            bottom = matrix[y+1:,  x]
            views = [
                left[::-1], 
                right, 
                top[::-1], 
                bottom
            ]
            
            view_lengths = []
            for view in views:
                taller = view >= value
                if not np.any(taller):
                    view_lengths.append(len(view))
                else:
                    view_lengths.append(np.argmax(taller) + 1)
            score = np.prod(view_lengths)
            if score > best_score:
                best_score = score
    return best_score    
            
result = naive(matrix=rows)
print(result)


