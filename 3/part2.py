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
idx = 0
with open(sys.argv[1], 'r') as fd:
    unique = set()

    for line in fd.readlines():
        line = line.replace('\n', '')
        if idx % 3 == 0:
            unique = set(line)
        else:
            unique &= set(line)
        if idx % 3 == 2:
            badge = list(unique)[0]
            unique = set()
            prio = get_priority(badge)
            total += prio
        idx += 1
print(f'total={total}')