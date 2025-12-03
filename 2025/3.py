import sys
import numpy as np


banks = []
with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        banks.append(list(map(int, line.strip())))

def find_max_in_bank(bank):
    max_idx1 = np.argmax(bank[:-1])
    max_idx2 = max_idx1 + 1 + np.argmax(bank[max_idx1+1:])
    return bank[max_idx1] * 10 + bank[max_idx2]

result = 0
for bank in banks:
    maxim = find_max_in_bank(bank)
    print(maxim)
    result += maxim

print("result: ", result)