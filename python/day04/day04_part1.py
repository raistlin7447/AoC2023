import re

total = 0
with open('day04_input.txt') as f:
    for line in f:
        _, winning, have = re.split(r"[:|]", line)
        winning = winning.split()
        have = have.split()

        win_count = 0
        for win in winning:
            if win in have:
                win_count += 1

        if win_count:
            total += 2**(win_count-1)

print(total)
