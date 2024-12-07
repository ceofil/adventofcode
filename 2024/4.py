import numpy as np

with open('inputs\\4') as fd:
    content = fd.read()

m = content.split('\n')
needle = "XMAS"

def search_pos_dir(_pos, dir):
    pos = _pos.copy()
    for character in needle:
        if not 0 <= pos[1] < len(m):
            return False
        if not 0 <= pos[0] < len(m[0]):
            return False
        if m[pos[1]][pos[0]] != character:
            return False
        pos += dir
    return True

dirs = [
    np.array([0, 1]),
    np.array([1, 1]),
    np.array([1, 0]),
    np.array([1, -1]),
    np.array([0, -1]),
    np.array([-1, -1]),
    np.array([-1, 0]),
    np.array([-1, 1]),
]
res = 0
for y in range(0, len(m)):
    for x in range(0, len(m[0])):
        pos = np.array([x,y])
        for dir in dirs:
            if search_pos_dir(pos, dir):
                res += 1

print(res)            

