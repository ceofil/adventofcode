import sys
import numpy as np
from tqdm import tqdm
from itertools import combinations
data = []
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        str_lights, *str_buttons, str_j = line.strip().split(' ')
        str_lights = str_lights.strip('[]')

        lights = np.array([1 if i =='#' else 0 for i in str_lights])

        buttons = []
        for str_btn in str_buttons:
            indices = list(map(int, str_btn.strip('()').split(',')))
            btn = np.zeros_like(lights)
            btn[indices] = 1
            buttons.append(btn)

        str_j = str_j.strip(r'{}')

        data.append((lights, buttons, str_j))


result = 0
for target_lights, buttons, j in data:
    if sum(target_lights) == 0:
        continue
    for n_comb in range(1,len(buttons)+1):
        found = False
        for button_subset in combinations(buttons, n_comb):
            lights = np.zeros_like(target_lights)
            for button in button_subset:
                lights = np.bitwise_xor(lights, button)
            if np.all(np.equal(lights, target_lights)):
                result += n_comb
                found = True
                break
        if found:
            break
print('result', result)