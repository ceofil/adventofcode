import sys

def get_marker_idx(line, n):
    for i in range(len(line)):
        if len(set(line[i:i+n])) == n:
            return i + n
    return 'pls'

with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        line = line.replace('\n', '')
        marker_idx = get_marker_idx(line, 14)
        print(marker_idx)