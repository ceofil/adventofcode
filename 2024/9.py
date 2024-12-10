

with open("inputs/9", "r") as fd:
    c = fd.read()

c = list(map(int, c))
lens = c[::2]
spaces = c[1::2]
print(lens)
print(spaces)

res = 0
idx = 0
LEFT_ID = 0
RIGHT_ID = len(lens) - 1
SPACE_IDX = 0
from_left = True

finished = False
while not finished:
    if from_left:
        for _ in range(lens[LEFT_ID]):
            res += idx * LEFT_ID
            idx += 1
        lens[LEFT_ID] = 0
        LEFT_ID += 1
        from_left = False
    else:
        if SPACE_IDX < len(spaces):
            for _ in range(spaces[SPACE_IDX]):
                if lens[RIGHT_ID] == 0:
                    RIGHT_ID -= 1
                if lens[RIGHT_ID] == 0:
                    finished = True
                    break
                lens[RIGHT_ID] -= 1
                res += idx * RIGHT_ID
                idx += 1
            SPACE_IDX += 1
        from_left = True
print(res)