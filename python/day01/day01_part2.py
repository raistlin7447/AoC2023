import re

spelled_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

r = r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"
total = 0
with open('day01_input.txt') as f:
    for line in f:
        results = [m[1] for m in re.finditer(r, line)]
        numbers = [spelled_map[i] if i in spelled_map else int(i) for i in results]
        value = numbers[0] * 10 + numbers[-1]
        total += value

print(total)
