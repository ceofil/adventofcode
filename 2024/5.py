with open('inputs\\5', 'r') as fd:
    content = fd.read()

rules, updates = content.split('\n\n')
rules = rules.split('\n')
rules = [rule.split('|') for rule in rules]
updates = updates.split('\n')

res = 0
for update in updates:
    pages = update.split(',')
    valid = True
    for left, right in rules:
        try:
            idxLeft = pages.index(left)
            idxRight = pages.index(right)
        except Exception as _:
            continue
        if not idxLeft < idxRight:
            valid = False
            break
    if valid:
        res += int(pages[len(pages)//2])
print(res)