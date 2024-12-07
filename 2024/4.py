import numpy as np

with open('inputs\\4') as fd:
    content = fd.read()

m = content.split('\n')
needle = "MAS"

def posInside(pos):
    if not 0 <= pos[1] < len(m):
        return False
    if not 0 <= pos[0] < len(m[0]):
        return False
    return True


def diag(pos, dir):
    word = ""
    for i in range(-1, 2):
        ipos = pos + dir * i
        if not posInside(ipos):
            return False
        word += m[ipos[1]][ipos[0]]
    if word == needle or word[::-1] == needle:
        return True
    return False
res = 0
dir1 = np.array([1,1])
dir2 = np.array([-1,1])
for y in range(0, len(m)):
    for x in range(0, len(m[0])):
        pos = np.array([x,y])
        if diag(pos, dir1) and diag(pos, dir2):
            res += 1
print(res)            

