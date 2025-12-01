

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
    old_cursor = cursor
    cursor += dirrection * magnitude
    if cursor <= 0:
        result += abs(cursor)//100 + 1
        if old_cursor == 0:
            result -= 1  # already counted
    if cursor >= 100:
        result += cursor//100

    cursor = cursor % 100

print("result:", result)