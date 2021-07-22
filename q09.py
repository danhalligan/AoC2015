from itertools import permutations
import re 
dat = open("inputs/q09.txt", "r").read().splitlines()

dist = {}
places = set()
for x in dat:
    p = re.split(r'\s(to|=)\s', x)
    dist[(p[0], p[2])] = int(p[4])
    dist[(p[2], p[0])] = int(p[4])
    places.update([p[0], p[2]])

n = len(places)
tot = [
    sum([dist[(poss[i], poss[i+1])] for i in range(n-1)])
    for poss in permutations(places)
]

print("Part1:", min(tot))
print("Part2:", max(tot))
