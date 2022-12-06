import sys

a = ord('a')
A = ord('A')
z = ord('z')
Z = ord('Z')

def get_priority(ch):
    ch = ord(ch)
    if a <= ch <= z:
        return ch - a + 1
    return ch - A + 27

total = 0
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        line = line.replace('\n', '')
        length = len(line) // 2
        first = line[:length]
        second = line[length:]
        diff = list(set(first) & set(second))[0]
        prio = get_priority(diff)
        total += prio
print(f'total={total}')