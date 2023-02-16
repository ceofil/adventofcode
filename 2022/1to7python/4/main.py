import sys


def a_contains_b(a_start, a_end, b_start, b_end):
    return b_start >= a_start and b_end <= a_end

def overlaps(a_start, a_end, b_start, b_end):
    return b_start <= a_start <= b_end or b_start <= a_end <= b_end or \
           a_start <= b_start <= a_end or a_start <= b_end <= a_end

total = 0
overlaps_at_all = 0
with open(sys.argv[1]) as fd:
    for line in fd.readlines():
        line = line.replace('\n', '')
        a, b = line.split(',')
        a_start, a_end = map(int, a.split('-'))
        b_start, b_end = map(int, b.split('-'))
        contained = a_contains_b(a_start, a_end, b_start, b_end) or \
                    a_contains_b(b_start, b_end, a_start, a_end) 
        if contained:
            total += 1
        if overlaps(a_start, a_end, b_start, b_end):
            overlaps_at_all += 1
print('part1: ', total)       
print('part2: ', overlaps_at_all)