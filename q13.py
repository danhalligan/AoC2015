import re
import itertools
from itertools import permutations
from collections import defaultdict

lines = open('inputs/q13.txt').read().splitlines()

# Part 1
rules = defaultdict(dict)
for line in lines:
    s = line.split()
    who = s[0]
    to = s[10][:-1]
    val = int(s[3]) if s[2] == 'gain' else -int(s[3])
    rules[who].update({to: val})

def score(p):
    s = 0
    for i in range(len(p)):
        n = (i + 1) % len(p)
        s += rules[p[i]][p[i-1]] + rules[p[i]][p[n]]
    return s

perms = list(permutations(rules.keys()))
print("Part1", max([score(p) for p in perms]))

# Part 2
people = set(rules.keys())
for n in people:
    rules['me'][n] = 0
    rules[n]['me'] = 0

perms = list(permutations(list(rules.keys())))
print("Part2", max([score(p) for p in perms]))
