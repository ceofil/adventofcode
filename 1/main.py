import heapq
import random

calories = []
input_file = 'input'
with open(input_file, 'r') as fd:
    currentSum = 0
    maxSum = 0
    for line in fd.readlines():
        try:
            nr = int(line)
            currentSum += nr
        except Exception as _:
            calories.append(currentSum)
            currentSum = 0
    calories.append(currentSum)


print(f'maxSum={max(calories)}')
print(f'maxSumTop3={sum(heapq.nlargest(3, calories))}')