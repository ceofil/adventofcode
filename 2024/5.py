with open('inputs\\5', 'r') as fd:
    content = fd.read()

rules, updates = content.split('\n\n')
rules = rules.split('\n')
rules = set([tuple(rule.split('|')) for rule in rules])
updates = updates.split('\n')

invalid_updates = []
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
    if not valid:
        invalid_updates.append(update)




def bubble_sort_update(update):
    pages = update.split(',')
    for ii in range(len(pages) - 1):
        for jj in range(ii + 1, len(pages)):
            if (pages[jj],pages[ii]) in rules:
                pages[ii],pages[jj] = pages[jj],pages[ii]
    return pages

res = 0
for update in invalid_updates:
    sorted_pages = bubble_sort_update(update)
    res += int(sorted_pages[len(sorted_pages)//2])
print(res)