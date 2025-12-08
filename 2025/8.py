import sys
import numpy as np
from tqdm import tqdm

data = []
file = sys.argv[1]
n_connections = 10 if file.endswith('.test') else 1000
with open(file, 'r') as fd:
    for line in fd:
        numbers = map(float, line.strip().split(','))
        data.append(np.array(list(numbers)))

data = np.array(data)

diff = data[:, np.newaxis, :] - data[np.newaxis, :, :]
dists = np.linalg.norm(diff, axis=-1)

indeces = [(i1, i2) for i1 in range(len(data)) for i2 in range(i1)]
indeces = sorted(indeces, key=lambda x: dists[x[0], x[1]])

edges = np.zeros((len(data), len(data)), dtype=int)
for i1, i2 in indeces:
    edges[i1, i2] = 1
    edges[i2, i1] = 1

    visited = set()

    clusters = []
    for start_node in range(len(data)):
        if start_node in visited:
            continue
        visited.add(start_node)
        cluster = [start_node]
        stack = [start_node]
        while stack:
            node = stack.pop()
            neighbors = np.where(edges[node] == 1)[0]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    cluster.append(int(neighbor))
        clusters.append(cluster)

    if len(clusters) == 1 and len(clusters[0]) == len(data):
        print(data.shape, data[i2,0])

        print("result:", data[i1,0] * data[i2,0])
        break
    else:
        print(f'{len(data)-len(clusters)}/{len(data)}')