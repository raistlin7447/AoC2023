import re
from itertools import cycle
from math import lcm

map = {}
with open('day08_input.txt') as f:
    lines = f.readlines()
    instructions = lines[0].strip()

    for line in lines[2:]:
        [key, _, _, _, left, _, right, _] = re.split(r"[=(,) ]", line.strip())
        map[key] = (left, right)

circuit_counts = []

for node in map.keys():
    location = node
    if location[2] != "A":
        continue

    steps = 0
    for direction in cycle(instructions):
        steps += 1
        location = map[location][0] if direction == "L" else map[location][1]
        if location[2] == "Z":
            circuit_counts.append(steps)
            break

print(lcm(*circuit_counts))