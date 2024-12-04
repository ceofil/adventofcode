import numpy as np

def wholeReportIsSafe(report):
    diff = np.diff(report)
    signs = np.sign(diff)
    if not (np.all(signs == 1) or np.all(signs == -1)):
        return False
    
    adiff = np.abs(diff)
    if not np.sum(adiff < 1) + np.sum(adiff > 3) == 0:
        return False
    return True

def reportIsPartiallySafe(report):
    if wholeReportIsSafe(report):
        return True
    for idx in range(report.shape[0]):
        if wholeReportIsSafe(np.delete(report, idx)):
            return True
    return False

res = 0
with open('inputs\\2') as fd:
    for line in fd.readlines(): 
        report = np.array([int(x) for x in line.split(' ')])
        if reportIsPartiallySafe(report):
            res += 1

print(res)  