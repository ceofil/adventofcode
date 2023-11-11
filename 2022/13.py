import sys
from enum import Enum
from functools import cmp_to_key
class Comparison(Enum):
    LOWER = -1
    EQUAL = 0
    GREATER = 1

packets = []
with open(sys.argv[1], 'r') as fd:
    data = fd.read()
    pairs = data.split('\n\n')
    pairs = [pair.split('\n') for pair in pairs]
    for pair in pairs:
        packets.extend(pair)


def order(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l ==  r:
            return Comparison.EQUAL
        if l < r:
            return Comparison.LOWER
        if l > r: 
            return Comparison.GREATER
    if isinstance(l, list) and isinstance(r, list):
        for left, right in zip(l, r):
            result = order(left, right)
            if not result == Comparison.EQUAL:
                return result
        return order(len(l), len(r))
    if isinstance(l, int) and isinstance(r, list):
        return order([l], r)
    if isinstance(l, list) and isinstance(r, int):
        return order(l, [r])
    raise Exception("should be reached")
        
    
# total = 0

# for index, (left, right) in enumerate(pairs, start=1):
#     print(f'{index=}')
#     l = eval(left)
#     r = eval(right)
#     result = order(l, r)
#     if result == Comparison.LOWER:
#         print('in order')
#         total += index 
#     else:
#         print('not in order')   
#     print(l)
#     print(r)
#     print('----')
        
# print(f'{total=}')

two_divider = [[2]]
six_divider = [[6]]
packets = [eval(packet) for packet in packets]
packets.append(two_divider)
packets.append(six_divider)
packets.sort(key=cmp_to_key(lambda l, r: order(l,r).value))

two_index = None
six_index = None
for index, packet in enumerate(packets, start=1):
    if two_index is None and order(packet, two_divider) == Comparison.EQUAL:
        two_index = index
    if six_index is None and order(packet, six_divider) == Comparison.EQUAL:
        six_index = index

print(f'divider prod = {two_index*six_index}')

    