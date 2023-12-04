import re
from collections import defaultdict

cards = defaultdict(int)

with open('day04_input.txt') as f:
    for line in f:
        _, card, winning, have = re.split(r"Card |[:|]", line)
        card = int(card)
        winning = winning.split()
        have = have.split()

        cards[card] += 1

        win_count = 0
        for win in winning:
            if win in have:
                win_count += 1

        if win_count:
            for i in range(card+1, card+win_count+1):
                cards[i] += cards[card]

print(sum(cards.values()))
