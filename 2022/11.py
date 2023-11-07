import sys
import numpy as np 
from collections import namedtuple
from queue import Queue
from typing import List
from tqdm import tqdm

blueprints = []
with open(sys.argv[1], 'r') as fd:
    bp = []
    for line in fd.readlines():
        if line == '\n':
            blueprints.append(bp)
            bp = []
            continue
        bp.append(line)
    blueprints.append(bp)

Monkey = namedtuple("Monkey", ["items", "operation", "test", "if_true", "if_false"])
monkeyz: List[Monkey] = []
for bp in blueprints:
    items = Queue()
    for i in bp[1].rstrip('\n').split(':')[1].split(','):
        items.put(int(i))
    operation = bp[2].rstrip('\n').split('=')[1]
    test = int(bp[3].split('by')[1])
    if_true = int(bp[4].split('monkey')[1])
    if_false = int(bp[5].split('monkey')[1])
    monkeyz.append(
        Monkey(
            items=items, 
            operation=operation, 
            test=test, 
            if_true=if_true, 
            if_false=if_false
        )
    )

test_product = np.prod([m.test for m in monkeyz])


ROUNDS = 10_000
inspected = [0 for _ in range(len(monkeyz))]
for _ in tqdm(range(ROUNDS)):
    for index, m in enumerate(monkeyz):
        while not m.items.empty():
            worry = m.items.get()
            worry = eval(m.operation.replace('old', str(worry)))
            worry = worry % test_product
            if worry % m.test == 0:
                throw_to = m.if_true
            else:
                throw_to = m.if_false
            monkeyz[throw_to].items.put(worry)
            inspected[index] += 1

print(inspected)
inspected.sort()
print(f'result={inspected[-1] * inspected[-2]}')
                
     
     
    