
from itertools import combinations
from math import prod

dat = open("inputs/q02.txt", "r").read().split()
dat = [list(map(int, x.split("x"))) for x in dat]

# part 1
tot = 0
for x in dat:
    p = [i*j for i, j in combinations(x, 2)]
    tot += min(p) + sum(p)*2

print(tot)

# part 2
tot = 0
for x in dat:
    x.sort()
    tot += sum(x[0:2])*2 + prod(x)

print(tot)
