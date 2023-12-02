import re
from collections import defaultdict
from math import prod

find_dice = r"(?P<count>\d+) (?P<color>red|green|blue)"

total = 0
with open('day02_input.txt') as f:
    for line in f:
        max_of_color = defaultdict(int)
        match = re.finditer(find_dice, line)
        for m in match:
            count = int(m.group("count"))
            color = m.group("color")
            max_of_color[color] = max(max_of_color[color], count)
        total += prod(max_of_color.values())

print(total)
