from dataclasses import dataclass, field
from itertools import combinations
from typing import Tuple


@dataclass
class SkyMap:
    grid: list[list[int]]
    galaxies: list[Tuple[int, int]] = field(default_factory=list)

    def num_rows(self):
        return len(self.grid)

    def num_cols(self):
        return len(self.row(0))

    def row(self, row_index):
        return self.grid[row_index]

    def col(self, col_index):
        return [row[col_index] for row in self.grid]

    def is_row_empty(self, row_index):
        return sum(self.row(row_index)) == 0

    def is_col_empty(self, col_index):
        return sum(self.col(col_index)) == 0

    def expand_universe(self):
        new_grid = []

        for row_index, row in enumerate(self.grid):
            new_grid.append(row)
            if self.is_row_empty(row_index):
                new_grid.append(row.copy())

        empty_cols = []
        for i in range(self.num_cols()):
            if self.is_col_empty(i):
                empty_cols.append(i)

        empty_cols.reverse()
        for row in new_grid:
            for empty_col in empty_cols:
                row.insert(empty_col, 0)

        self.grid = new_grid

    def populate_galaxies(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.grid[i][j]:
                    self.galaxies.append((i, j))

    def __str__(self):
        as_str = ""
        for row in self.grid:
            as_str += "".join(["#" if i else "." for i in row]) + "\n"
        return as_str


with open('day11_input.txt') as f:
    lines = f.readlines()
    sky_map = SkyMap([[0 if i == "." else 1 for i in l.strip()] for l in lines])


sky_map.expand_universe()
sky_map.populate_galaxies()

total = 0
for galaxy1, galaxy2 in combinations(sky_map.galaxies, 2):
    distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    total += distance

print(total)