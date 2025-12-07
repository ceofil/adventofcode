import sys
import numpy as np

result = 0
with open(sys.argv[1], 'r') as file:
    lines = file.read().splitlines()
pos = lines[0].index('S')
print(pos)

beams = np.zeros(len(lines[0]), dtype=int)
beams[pos] = 1

output_str = ''
for line in lines[1:]:
    print('------------')
    splitter = np.array([1 if c == '^' else 0 for c in line], dtype=int)
    print(sum(splitter))
    print(line)
    print(beams.astype(int), "beams")
    print(splitter, "splitter")
    new_beams = beams + splitter
    print(new_beams, "new_beams")
    intersection = np.copy(new_beams == 2)
    print(intersection.astype(int), "intersection")
    result += np.sum(intersection)
    split_idexes = np.where(intersection)[0]
    print(len(split_idexes))
    new_beams[intersection] = 0
    new_beams[split_idexes - 1] = 1
    new_beams[split_idexes + 1] = 1
    new_beams[np.where(splitter == 1)[0]] = 0
    beams = np.copy(new_beams)
    
    m = {
        0: '.',
        1: '|',
    }
    str_beams = [m.get(b, '?') for b in beams]
    for i in range(splitter.shape[0]):
        if splitter[i] == 1:
            str_beams[i] = '^'
    str_beams= ''.join(str_beams)
    output_str += str_beams + '\n'
    print(str_beams)

with open('output.txt', 'w') as out_file:
    out_file.write(output_str)
    
print("result:", result)
