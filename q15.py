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

# yield combinations of k numbers that sum to 100
def ncomb(n, k, j=0):
    if k <= 1:
        yield [n-j]
    else:
        for i in range(n+1-j):
            for a, lst in product([i], ncomb(n, k-1, j+i)):
                yield lst + [a]

def scores():
    for tsp in ncomb(100, 4):
        score = 1
        for key in keys:
            score *= kscore(key, tsp)
            if score == 0: break
        if score == 0: continue
        yield [score, kscore('calories', tsp)]


lines = open('inputs/q15.txt').read().splitlines()
ing = [parse_line(line) for line in lines]
keys = ['durability', 'capacity', 'texture', 'flavor']

scores = list(scores())
print("Part1:", max(x for x, _ in scores))
print("Part2:", max(x for x, c in scores if c == 500))
