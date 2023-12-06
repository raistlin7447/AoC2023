import math

with open('day06_input.txt') as f:
    lines = f.read().splitlines()
    times = [int("".join([i for i in lines[0].split() if i.isnumeric()]))]
    dists = [int("".join([i for i in lines[1].split() if i.isnumeric()]))]

    total_wins = []
    for i, time in enumerate(times):
        wins = 0
        for attempt in range(1, time+1):
            speed = attempt
            remaining_time = time-attempt
            distance = remaining_time * speed
            if distance > dists[i]:
                wins += 1

        total_wins.append(wins)

    print(math.prod(total_wins))