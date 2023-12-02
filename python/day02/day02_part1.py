import re

max_colors = {
    "red": 12,
    "green": 13,
    "blue": 14
}

find_dice = r"(Game (?P<game>\d+):)? (?P<count>\d+) (?P<color>red|green|blue)"

total = 0
with open('day02_input.txt') as f:
    for line in f:
        match = re.finditer(find_dice, line)
        for m in match:
            if m.group("game"):
                game = int(m.group("game"))
            count = int(m.group("count"))
            color = m.group("color")
            if count > max_colors[color]:
                break
        else:
            total += game

print(total)
