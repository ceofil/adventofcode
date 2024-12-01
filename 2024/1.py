
first = []
second = []
with open('inputs\\1') as fd:
    for line in fd.readlines():
        items = line.split(' ')
        first.append(int(items[0]))
        second.append(int(items[-1]))
first.sort()
second.sort()

res1 = 0
for f, s in zip(first, second):
    res1 += abs(s - f)

res2 = 0
cache = dict()
for f in first:
    if f in cache:
        score = cache[f]
    else:
        score = second.count(f)
        cache[f] = score 
    res2 += score * f
print(res1)
print(res2)
    