total = 0
with open('day01_input.txt') as f:
    for line in f:
        numbers = [int(i) for i in line if i.isdigit()]
        value = numbers[0] * 10 + numbers[-1]
        total += value

print(total)
