from itertools import combinations
from math import prod

# passenger compartment packages must sum to target and have the fewest 
# packages.
def valid(dat, target):
    min_len = 1000
    for n in range(len(dat)):
        if n > min_len: continue
        for c1 in combinations(dat, n):
            if sum(c1) != target: continue
            min_len = len(c1)
            yield c1

dat = open('inputs/q24.txt').read().splitlines()
dat = [int(x) for x in dat]

print("Part1:", min([prod(x) for x in valid(dat, sum(dat)/3)]))
print("Part2:", min([prod(x) for x in valid(dat, sum(dat)/4)]))
