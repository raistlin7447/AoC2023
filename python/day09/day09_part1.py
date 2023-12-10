import itertools

with open('day09_input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        sequence = [[int(i) for i in line.split()]]
        current = sequence[0]
        last_item_total = 0

        while sum(current) != 0:
            last_item_total += current[-1]
            pairs = itertools.pairwise(current)
            current = []
            for first, second in pairs:
                current.append(second - first)
            sequence.append(current)

        total += last_item_total

    print(total)