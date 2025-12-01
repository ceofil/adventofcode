

data = []
with open('inputs/1', 'r') as fd:
    for line in fd:
        no_newline = line.strip().lower()
        dirrection = 1 if no_newline[0] == 'r' else -1
        magnitude = int(no_newline[1:])
        data.append((dirrection, magnitude))

cursor = 50
result = 0
for dirrection, magnitude in data:
    cursor += dirrection * magnitude
    cursor = cursor % 100
    if cursor == 0:
        result += 1
    print(cursor)
print("result:", result)