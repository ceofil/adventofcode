import sys
import numpy as np

result = 0
with open(sys.argv[1], 'r') as file:
    lines = file.read().splitlines()
    transposed = list(zip(*lines))

temp_result = 0
temp_op = ''
for *line, op in transposed:
    clean_line = ''.join(line).strip()
    if clean_line == '':
        result += temp_result
        print("temp_result", temp_result)
        continue
    number = int(clean_line)
    if op != ' ':
        temp_op = op
        temp_result = 1 if op == '*' else 0
    if temp_op == '+':
        temp_result += number
    else:
        temp_result *= number
result += temp_result
print("result:", result)
