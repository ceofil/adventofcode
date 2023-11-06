import numpy as np
import sys



cycle = 0
value = 1

with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        instruction = line.rstrip('\n')
        cycles = 1
        to_add = 0
        if not instruction == "noop":
            cycles = 2
            to_add = int(instruction.split(' ')[1])
        for cycle_diff in range(cycles):
            cycle += 1
            column = (cycle - 1) % 40
            if np.abs(column - value) <= 1:
                print('#', end='')
            else:
                print('.', end='')
            if cycle % 40 == 0:
                print('') 
            
        value += to_add
