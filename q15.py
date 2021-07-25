import re
from math import prod
from itertools import permutations, product

def parse_line(line):
    ingredient = re.search(r'(\w+):', line).group(1)
    r = re.compile(r'(\w+) (-*\d+)')
    dat = dict([a, int(x)] for a, x in r.findall(line))
    return dat

def kscore(key, tsp):
    return max(sum(ing[i][key]*tsp[i] for i in range(len(ing))), 0)

lines = open('inputs/q15.txt').read().splitlines()
ing = [parse_line(line) for line in lines]
keys = ['durability', 'capacity', 'texture', 'flavor']

#-------------------------------------------------------------------------------
## 1st ATTEMPT
# def score(ing, tsp):
#     vals = [kscore(key, tsp) for key in keys]
#     cals = sum(ing[i]['calories']*tsp[i] for i in range(len(ing)))
#     return [prod(vals), cals]

# result = [
#     score(ing, seq) 
#     for seq in permutations(range(101), 4) 
#     if sum(seq) == 100
# ]

# print("Part1:", max(x for x, _ in result))
# print("Part2:", max([v for v, c in result if c == 500]))


#-------------------------------------------------------------------------------
## 2nd ATTEMPT
# def findmax():
#     for a in range(101):
#         for b in range(101 - a):
#             for c in range(101 - a - b):
#                 d = 100 - a - b - c
#                 score = prod(kscore(key, [a,b,c,d]) for key in keys)
#                 if score == 0: continue
#                 yield [score, kscore('calories', [a,b,c,d])]


# print("Part1:", max(x for x, _ in findmax()))
# print("Part2:", max(x for x, c in findmax() if c == 500))


#-------------------------------------------------------------------------------
## and with less hardcoding!
def seq(n, k, j=0):
    if k <= 1:
        yield [n-j]
    else:
        for i in range(n+1-j):
            for a, lst in product([i], seq(n, k-1, j+i)):
                yield lst + [a]

def scores():
    for tsp in seq(100, 4):
        score = 1
        for key in keys:
            score *= kscore(key, tsp)
            if score == 0: break
        if score == 0: continue
        yield [score, kscore('calories', tsp)]

scores = list(scores())
print("Part1:", max(x for x, _ in scores))
print("Part2:", max(x for x, c in scores if c == 500))
