from tqdm import tqdm
import numpy as np
import itertools


with open("inputs/8", "r") as fd:
    m = [list(line.replace("\n", "")) for line in fd.readlines()]


freq = dict()

h = len(m)
w = len(m[0])
for y in range(h):
    for x in range(w):
        p = m[y][x]
        if p == ".":
            continue
        if p not in freq:
            freq[p] = []
        freq[p].append(np.array([x,y]))


def insideMap(node):
    return 0 <= node[0] < w and 0 <= node[1] < h

def getAnti(n1, n2):
    dif = n1 - n2
    antis = []
    for n, factor in zip([n1, n2], [1,-1]):
        nextn = n
        while insideMap(nextn):
            antis.append(nextn)
            nextn = nextn + dif * factor
    return antis

def processOneFrequency(nodes):
    anti = []
    for pair in itertools.combinations(nodes, 2):
        anti.extend(getAnti(*pair))
    return anti

all_anti = []
for f, nodes in freq.items():
    frequency_anti = processOneFrequency(nodes)
    all_anti.extend(frequency_anti)

uniq = set([(int(p[0]),int(p[1])) for p in all_anti])
valid_uniq = [anti for anti in uniq if insideMap(anti)]
print(len(valid_uniq))
