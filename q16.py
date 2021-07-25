import re
from operator import gt, lt, eq

def parse_line(line):
    name = re.search(r'(\w+):', line).group(1)
    r = re.compile(r'(\w+): (\d+)')
    dat = dict([a, int(x)] for a, x in r.findall(line))
    dat['num'] = name
    return dat

lines = open('inputs/q16.txt').read().splitlines()
sues = [parse_line(line) for line in lines]

requirements = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

for k in requirements.keys():
    sues = [d for d in sues if k not in d or d[k] == requirements[k]]

print("Part1:", sues[0]['num'])


def op(k):
    if k in ['cats', 'trees']: return gt
    elif k in ['pomeranians', 'goldfish']: return lt
    else: return eq

sues = [parse_line(line) for line in lines]

for k in requirements.keys():
    sues = [d for d in sues if k not in d or op(k)(d[k], requirements[k])]

print("Part2:", sues[0]['num'])
