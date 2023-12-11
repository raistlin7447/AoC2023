left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

adjacent = {
    "|": (up, down),
    "-": (left, right),
    "L": (up, right),
    "J": (up, left),
    "7": (down, left),
    "F": (down, right),
    ".": (),
    "S": (up, right, down, left)
}

connect_to_s = {
    up: ["|", "7", "F"],
    right: ["-", "J", "7"],
    down: ["|", "L", "J"],
    left: ["-", "L", "F"]
}

with open('day10_input.txt') as f:
    lines = f.readlines()
    map = [l.strip() for l in lines]

start = None
for i, row in enumerate(map):
    for j, col in enumerate(row):
        if col == "S":
            start = (i, j)
            break
    if start:
        break

paths = []
queue = [(start, [start])]
while queue:
    ((row, col), path) = queue.pop(0)
    char = map[row][col]
    for row_offset, col_offset in adjacent[char]:
        new_row = row + row_offset
        new_col = col + col_offset
        new = (new_row, new_col)

        if char == "S":
            if map[new_row][new_col] not in connect_to_s[(row_offset, col_offset)]:
                continue

        if new in path and new != start:
            continue
        if new == start:
            paths.append(path + [new])
        else:
            queue.append((new, path + [new]))

print(len(paths[-1]) // 2)
