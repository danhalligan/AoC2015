from itertools import cycle, accumulate, islice
from collections import Counter

def travel(s):
    name = s[0]
    speed, duration, rest = [int(s[i]) for i in [3, 6, 13]]
    n = int(2503 / (duration+rest))
    r = min(2503 % (duration+rest), duration) 
    return (n*duration + r) * speed

lines = open('inputs/q14.txt').read().splitlines()
print("Part1:", max(travel(line.split()) for line in lines))


def location(s):
    name = s[0]
    speed, duration, rest = [int(s[i]) for i in [3, 6, 13]]
    period = [speed]*duration + [0]*rest
    return accumulate(islice(cycle(period), 2503))

locs = [location(line.split()) for line in lines]
points = [x.index(max(x)) for x in zip(*locs)]
print("Part2:", max(Counter(points).values()))
