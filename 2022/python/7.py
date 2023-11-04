import sys
import json

def pp(_dict):
    print(json.dumps(_dict, indent=4))

commands = []
with open(sys.argv[1], 'r') as fd:
    result = []
    instruction = ''
    for line in fd.readlines():
        if not line.startswith('$'):
            result.append(line)
        else:
            if instruction:
                commands.append((instruction, result))
            instruction = line
            result = []
    commands.append((instruction, result))

tree = {
    '/': dict()
}

def get_node(tree, path):
    curr_node = tree
    for key in path:
        curr_node = curr_node[key]
    return curr_node
    

current_path = ['/']
for instruction, result in commands[1:]:
    instruction_parts = instruction.split()
    command = instruction_parts[1]
    args = instruction_parts[2:]
    if command == 'ls':
        for file in result:
            descr, name = file.split()
            node = get_node(tree, current_path)
            if descr == 'dir':
                node[name] = dict()
            else:
                node[name] = int(descr)
    if command == 'cd':
        arg = args[0]
        if arg == '..':
            current_path = current_path[:-1]
        else:
            current_path.append(arg)

# pp(tree)


def get_dir_size(tree):
    # curr_node = tree
    total = 0
    nodes_to_visit = [tree]
    while nodes_to_visit:
        new_nodes = []
        for node in nodes_to_visit:
            for key in node:
                if type(node[key]) == dict:
                    new_nodes.append(node[key])
                else:
                    total += node[key]
        nodes_to_visit = new_nodes
    return total

full = 70_000_000
current = get_dir_size(tree)
unused = full - current
needed = 30_000_000
limit = needed - unused

candidates = []
def get_part2_dirs(tree, limit=100_000):
    nodes_to_visit = [tree]
    candidates = []
    while nodes_to_visit:
        new_nodes = []
        for node in nodes_to_visit:
            if type(node) == dict:
                for key in node:
                    if type(node[key]) == dict:
                        dir_size = get_dir_size(node[key]) 
                        if dir_size >= limit:
                            candidates.append(dir_size)
                    new_nodes.append(node[key])    
        nodes_to_visit = new_nodes
    return candidates
# pp(t)
# print(get_dir_size(t))
# print(get_part2_dirs(tree))
print(min(get_part2_dirs(tree, limit=limit)))
