import numpy as np

# def isIncOrDec(report):
    

res = 0
with open('inputs\\2') as fd:
    for line in fd.readlines(): 
        report = [int(x) for x in line.split(' ')]
        diff = np.diff(report)
        signs = np.sign(diff)
        print(report)
        if not (np.all(signs == 1) or np.all(signs == -1)):
            print('not desc or asc')
            continue
        
        adiff = np.abs(diff)
        if not (np.all(adiff >= 1) and np.all(adiff <= 3)):
            print('not 1 <= adiff <= 3')
            continue
        res += 1

print(res)  