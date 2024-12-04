import re




reg = r"mul\(([0-9]+,[0-9]+)\)"
creg = re.compile(reg)
with open('inputs\\3b.test') as fd:
    content = fd.read()
mulstrings = creg.findall(content)
res = 0
for mulstring in mulstrings:
    a,b = mulstring.split(',')
    res += int(a) * int(b)
print(res)