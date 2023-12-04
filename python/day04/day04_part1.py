import re

total = 0
with open('day04_input.txt') as f:
    for line in f:
        _, winning, have = re.split(r"[:|]", line)
        winning = set(winning.split())
        have = set(have.split())

        win_count = len(winning.intersection(have))
        if win_count:
            total += 2**(win_count-1)

print(total)
