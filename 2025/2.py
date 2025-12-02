import sys

ranges = []
with open(sys.argv[1], 'r') as file:
    str_ranges = file.read().replace('\n', '').split(',')
    for r in str_ranges:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))

result = 0
for r in ranges:
    for i in range(r[0], r[1] + 1):
        str_i = str(i)
        if len(str_i) % 2 != 0:
            continue
        mid = len(str_i) // 2
        if str_i[:mid] == str_i[mid:]:
            result += i
print("result:", result)