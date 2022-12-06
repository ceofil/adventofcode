import sys

reading_crates = True
crates = dict()
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        line = line.replace('\n', '')
        if line == '':
            continue
        if reading_crates:
            row = list(line)[1::4]
            if row[0].isnumeric():
                reading_crates = False
                continue
            for tower_idx, crate in enumerate(row, start=1):
                if crate.isalpha():
                    if tower_idx not in crates:
                        crates[tower_idx] = []
                    crates[tower_idx].insert(0, crate)
            continue
        quantity, from_idx, to_idx = map(int, line.split(' ')[1::2])
        crates[to_idx].extend(crates[from_idx][-quantity:])
        crates[from_idx] = crates[from_idx][:-quantity]
result = ''
for key in sorted(list(crates.keys())):
    result += crates[key][-1]
print(result)
