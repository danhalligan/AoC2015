import re
from random import shuffle

def replace_match(m, r, s):
    return s[:m.start()] + r + s[m.end():]

def allsubs(x, rep):
    l = list()
    for sub in rep:
        for m in re.finditer(sub[0], x):
            yield replace_match(m, sub[1], x)

def read(file="inputs/q19.txt"):
    codes, mol = open(file, "r").read().split("\n\n")
    mol = mol.rstrip()
    return mol, [tuple(code.split(" => ")) for code in codes.splitlines()]

rep = [('H', 'HO'), ('H', 'OH'), ('O', 'HH')]
len(set(allsubs('HOH', rep)))
len(set(allsubs('HOHOHO', rep)))

mol, rep = read()

print("Part1:", len(set(allsubs(mol, rep))))

def apply_transforms(mol, rep):
    count = 0
    while len(mol) > 1:
        start = mol
        for f, t in rep:
            mol, c = re.subn(t, f, mol)
            count += c
        if start == mol:
            return None
    return count

result = None
while result is None:
    shuffle(rep)
    result = apply_transforms(molecule, rep)

print("Part2:", result)

