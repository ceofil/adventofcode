import sys
import numpy as np
from tqdm import tqdm
from shapely.geometry import Point, Polygon

data = []
with open(sys.argv[1], 'r') as fd:
    for line in fd:
        numbers = map(float, line.strip().split(','))
        data.append(np.array(list(numbers)))


def compute_area_of_rectangle(p1, p2):
    lengths = np.abs(p1 - p2) + 1
    return np.prod(lengths)


areas = []
for i1, p1 in tqdm(enumerate(data), total=len(data)):
    for i2, p2 in enumerate(data[:i1]):
        area = compute_area_of_rectangle(p1, p2)
        areas.append(((i1,i2),area))
areas.sort(key=lambda a: a[1], reverse=True)


polygon = Polygon([tuple(p) for p in data])   
for (i1,i2), area in tqdm(areas):
    corenr1, corner2 = data[i1], data[i2]
    corner3 = np.array([corenr1[0], corner2[1]])
    corner4 = np.array([corner2[0], corenr1[1]])
    all_corners = [corenr1, corner2, corner3, corner4]
    rect = Polygon([tuple(p) for p in all_corners]) 
    if polygon.contains(rect):
        print("result:", area)
        break