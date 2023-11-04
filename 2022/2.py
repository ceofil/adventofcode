import sys
"""
enemy
    a - rock
    b - paper
    c - scissors

self
    x - rock 1
    y - paper 2
    z - scissors 3
"""
ROCK = 0
PAPER = 1
SCISSORS = 2

enemy = ['a', 'b', 'c']
this = ['x', 'y', 'z']

move_to_str = ['rock', 'paper', 'scissors']

LOSS = 0
DRAW = 3
WIN = 6
def outcome_score(enemy_move, this_move):
    if enemy_move == this_move:
        return DRAW
    if enemy_move == SCISSORS and this_move == ROCK:
        return WIN
    if enemy_move == ROCK and this_move == SCISSORS:
        return LOSS
    if this_move > enemy_move:
        return WIN
    return LOSS


def get_points_from_round(line):
    line = line.replace('\n', '')
    enemy_encrypted, this_encrypted = line.split(' ')
    enemy_move = enemy.index(enemy_encrypted.lower())
    this_move = this.index(this_encrypted.lower())
    score = this_move + 1 + outcome_score(enemy_move, this_move)
    # print(move_to_str[enemy_move], move_to_str[this_move], score)
    return score 

def part_two(line):
    line = line.replace('\n', '')
    enemy_encrypted, this_encrypted = line.split(' ')
    enemy_move = enemy.index(enemy_encrypted.lower())
    outcome = this.index(this_encrypted.lower()) * 3
    if outcome == DRAW:
        this_move = enemy_move
    elif outcome == LOSS:
        this_move = (enemy_move - 1) % 3
    else:
        this_move = (enemy_move + 1) % 3
    score = outcome + this_move + 1
    print(score, move_to_str[enemy_move], move_to_str[this_move])
    return score

total = 0
part_two_total = 0
with open(sys.argv[1], 'r') as fd:
    for line in fd.readlines():
        total += get_points_from_round(line)
        part_two_total += part_two(line)
print(f'total={total}')
print(f'partTwo={part_two_total}')