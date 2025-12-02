import sys
from tqdm import tqdm
ranges = []
with open(sys.argv[1], 'r') as file:
    str_ranges = file.read().replace('\n', '').split(',')
    for r in str_ranges:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))




result = 0
for r in tqdm(ranges):
    for i in range(r[0], r[1] + 1):
        str_i = str(i)

        for substr_len in range(1, len(str_i)//2 + 1):
            if len(str_i) % substr_len != 0:
                continue
            all_substrings = [str_i[j:j+substr_len] for j in range(0, len(str_i), substr_len)]
            if all(s == all_substrings[0] for s in all_substrings):
                result += i
                break
print("result:", result)