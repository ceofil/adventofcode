
first = []
second = []
with open('inputs\\1') as fd:
    for line in fd.readlines():
        items = line.split(' ')
        first.append(int(items[0]))
        second.append(int(items[-1]))
first.sort()
second.sort()

res = 0
for f, s in zip(first, second):
    res += abs(s - f)

print(res)
    