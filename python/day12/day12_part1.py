def count(springs, contigs):
    result = 0

    if not springs:
        # If there are no springs and no contigs remaining, this is valid
        if not contigs:
            result = 1
        else:
            result = 0

    elif not contigs:
        # If there are no contigs left, but there is still an unknown in the springs, this is invalid
        if "#" in springs:
            result = 0
        else:
            result = 1
    else:
        # Check for operational
        if springs[0] in [".", "?"]:
            result += count(springs[1:], contigs)

        # Check for damaged
        if springs[0] in ["#", "?"]:
            springs_left = contigs[0] <= len(springs)
            operational_in_front = "." in springs[:contigs[0]]
            num_springs_equals_contigs = len(springs) == contigs[0]
            if springs_left and not operational_in_front and (num_springs_equals_contigs or springs[contigs[0]] != "#"):
                result += count(springs[contigs[0] + 1:], contigs[1:])

    return result


spring_lines = []
with open('day12_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        springs, contiguous = line.split()
        contiguous = [int(i) for i in contiguous.split(",")]
        spring_lines.append((springs, contiguous))

total = 0
for spring_line in spring_lines:
    total += count(spring_line[0], spring_line[1])

print(total)