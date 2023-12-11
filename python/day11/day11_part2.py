from dataclasses import dataclass, field
from itertools import combinations
from typing import Tuple, Set


@dataclass
class SkyMap:
    grid: list[list[int]]
    galaxies: list[Tuple[int, int]] = field(default_factory=list)
    empty_rows: list[int] | Set[int] = field(default_factory=list)
    empty_cols: list[int] | Set[int] = field(default_factory=list)

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

    def populate_empties(self):
        for row_index, row in enumerate(self.grid):
            if self.is_row_empty(row_index):
                self.empty_rows.append(row_index)
        self.empty_rows = set(self.empty_rows)

        for col_index in range(self.num_cols()):
            if self.is_col_empty(col_index):
                self.empty_cols.append(col_index)
        self.empty_cols = set(self.empty_cols)

    def populate_galaxies(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.grid[i][j]:
                    self.galaxies.append((i, j))

    def distance(self, galaxy1, galaxy2):
        expansion_factor = 999999

        row_smaller, row_larger = sorted([galaxy1[0], galaxy2[0]])
        col_smaller, col_larger = sorted([galaxy1[1], galaxy2[1]])

        row_diff = row_larger - row_smaller
        col_diff = col_larger - col_smaller

        rows_crossed = set(range(row_smaller, row_larger + 1))
        cols_crossed = set(range(col_smaller, col_larger + 1))

        empty_rows_crossed = rows_crossed.intersection(self.empty_rows)
        empty_cols_crossed = cols_crossed.intersection(self.empty_cols)

        rows_expansion_diff = len(empty_rows_crossed) * expansion_factor
        cols_expansion_diff = len(empty_cols_crossed) * expansion_factor

        return row_diff + col_diff + rows_expansion_diff + cols_expansion_diff

    def __str__(self):
        as_str = ""
        for row in self.grid:
            as_str += "".join(["#" if i else "." for i in row]) + "\n"
        return as_str


with open('day11_input.txt') as f:
    lines = f.readlines()
    sky_map = SkyMap([[0 if i == "." else 1 for i in l.strip()] for l in lines])


sky_map.populate_empties()
sky_map.populate_galaxies()

total = 0
for galaxy1, galaxy2 in combinations(sky_map.galaxies, 2):
    distance = sky_map.distance(galaxy1, galaxy2)
    total += distance

print(total)