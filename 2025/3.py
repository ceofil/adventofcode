import sys
import numpy as np


banks = []
with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        banks.append(list(map(int, line.strip())))

def find_max_in_bank(bank):
    res = 0
    prev_idx = -1
    for k in list(range(12))[::-1]:
        idx = prev_idx + 1 + np.argmax(bank[prev_idx + 1:len(bank)-k])
        res = res * 10 + bank[idx]
        prev_idx = idx
    return res


result = 0
for bank in banks:
    maxim = find_max_in_bank(bank)
    print(maxim)
    result += maxim

print("result: ", result)