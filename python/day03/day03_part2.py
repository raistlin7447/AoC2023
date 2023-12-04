from dataclasses import dataclass

adjacent = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]

parts = []
grid = []
gear_ratios = []

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
            adjacent_parts = []
            for i, j in adjacent:
                r_check = row + i
                c_check = col + j
                if r_check >= 0 and c_check >= 0:
                    check_cell = grid[r_check][c_check]
                    if isinstance(check_cell, Part):
                        if check_cell not in adjacent_parts:
                            adjacent_parts.append(check_cell)
                        check_cell.valid = True
            if len(adjacent_parts) == 2:
                gear_ratios.append(adjacent_parts[0].number * adjacent_parts[1].number)

total_parts = sum(part.number for part in parts if part.valid is True)
total_gear_ratio = sum(gear_ratios)

print(f"{total_parts=}")
print(f"{total_gear_ratio=}")
