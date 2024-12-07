import re



do_regex = re.compile(r"don\'t\(\)|do\(\)")

with open('inputs\\3') as fd:
    content = fd.read()
content = "do()" + content
s = re.split(do_regex, content)
s = s[1:]
sep = re.findall(do_regex, content)

res = 0
compiled_mul_regex = re.compile(r"mul\(([0-9]+,[0-9]+)\)")
for string, separator in zip(s, sep, strict=True):
    if separator == "don't()":
        continue
    mul_regex = r"mul\(([0-9]+,[0-9]+)\)"
    mulstrings = compiled_mul_regex.findall(string)
    for mulstring in mulstrings:
        a,b = mulstring.split(',')
        res += int(a) * int(b)
print(res)