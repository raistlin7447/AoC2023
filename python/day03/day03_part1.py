from dataclasses import dataclass

adjacent = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]

parts = []
grid = []

@dataclass
class Part:
    number: int
    valid: bool = False

with open('day03_input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))

for row, row_data in enumerate(grid):
    for col, char in enumerate(row_data):
        if char.isnumeric():
            if col > 0 and isinstance(grid[row][col-1], Part):
                p = grid[row][col-1]
                p.number = int(str(p.number)+char)
                grid[row][col] = p
            else:
                new_part = Part(int(char))
                grid[row][col] = new_part
                parts.append(new_part)

for row, row_data in enumerate(grid):
    for col, char in enumerate(row_data):
        if not isinstance(char, Part) and char != ".":
            for i, j in adjacent:
                r_check = row + i
                c_check = col + j
                if r_check >= 0 and c_check >= 0:
                    check_cell = grid[r_check][c_check]
                    if isinstance(check_cell, Part):
                        check_cell.valid = True

total = sum(part.number for part in parts if part.valid is True)

print(total)
