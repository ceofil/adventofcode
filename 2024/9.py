

with open("inputs/9.test", "r") as fd:
    c = fd.read()

c = list(map(int, c))
lens = c[::2]
spaces = c[1::2]
if len(spaces) < len(lens):
    spaces.append(0)
print(lens)
print(spaces)



def shiftIdxToLeft(lens: list, spaces:list, lenIdx:int, spaceIdx:int):
    length = lens.pop(lenIdx)
    space = spaces.pop(lenIdx)
    spaces[spaceIdx] -= length
    spaces[lenIdx] += length
    lens.insert(spaceIdx+1, length)
    spaces.insert(spaceIdx, 0)

# 2333133121414131402

delta = 0
shiftIdxToLeft(lens, spaces, lenIdx=-1, spaceIdx=0)
print(lens)
print(spaces)