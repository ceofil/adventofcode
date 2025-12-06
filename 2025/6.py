import sys
import numpy as np

result = 0
with open(sys.argv[1], 'r') as file:
    lines = map(lambda l: l.split(), file.read().splitlines())
for *numbers_str, op in zip(*lines):
    numbers = list(map(int, numbers_str))
    if op == '+':
        result += sum(numbers)
    elif op == '*':
        result += np.prod(numbers)
print("result:", result)
