from tqdm import tqdm
import itertools

MULTIPLY = 0
SUM = 1
CONCAT = 2
ALL_OPERATORS = [MULTIPLY, SUM, CONCAT]


def compute(numbers, operators):
    total = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == MULTIPLY:
            total *= num
        elif op == SUM:
            total += num
        elif op == CONCAT:
            total = int(str(total)+str(num))
            
        else:
            raise Exception("wrong operator")
    return total

def check(result, numbers):
    for operators in itertools.product(ALL_OPERATORS, repeat=len(numbers)-1):
        if compute(numbers, operators) == result:     
            return True
    return False


def processLine(line):
    line = line.replace("\n", "")
    result, numbers = line.split(": ")
    result = int(result)
    numbers = [int(nr) for nr in numbers.split(" ")]
    if check(result, numbers):
        return result
    return 0


res = 0
with open("inputs/7", "r") as fd:
    for line in tqdm(list(fd.readlines())):
        res += processLine(line)

print(res)