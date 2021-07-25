from collections import defaultdict
from itertools import cycle, product, combinations

def read_items():
    lines = open("inputs/q21-items.txt", "r").read().splitlines()
    header = lines[0].split()
    tab = [dict(zip(header, line.split())) for line in lines[1:]]
    
    ints = ['Cost', 'Damage', 'Armor']
    items = defaultdict(list)
    for line in tab:
        for key in ints: line[key] = int(line[key])
        items[line['Class']] += [{k: line[k] for k in ['Item'] + ints}]
    
    items['Armor'] += [{'Item': 'None', 'Cost':0, 'Damage':0, 'Armor':0}]
    
    items['Ring'] += [{'Item': 'None', 'Cost':0, 'Damage':0, 'Armor':0}]
    items['Ring'] += [{'Item': 'None', 'Cost':0, 'Damage':0, 'Armor':0}]
    
    return items

def read_boss():
    boss = open("inputs/q21.txt", "r").read().splitlines()
    boss = dict(x.split(": ") for x in boss)
    for d in boss: boss[d] = int(boss[d])
    return boss

def round(a, b):
    b['Hit Points'] -= max(a['Damage'] - b['Armor'], 1)

def play(data):
    for a, b in cycle([['me', 'boss'], ['boss', 'me']]):
        round(data[a], data[b])
        if data[b]['Hit Points'] <= 0: break
    return data['me']['Hit Points'] > 0

def stat(kit, type):
    return sum(x[type] for x in kit)

def kits(items):
    for w in items['Weapon']:
        for a in items['Armor']:
            for rings in combinations(items['Ring'], 2):
                yield [w] + [a] + list(rings)

def stats(kit):
    return {
        'Hit Points': 100, 
        'Damage': stat(kit, 'Damage'), 
        'Armor': stat(kit, 'Armor')
    }

boss = read_boss()
items = read_items()

mincost = 100000
for kit in kits(items):
    if play({'boss': boss.copy(), 'me': stats(kit)}):
        mincost = min(stat(kit, 'Cost'), mincost)

print("Part1", mincost)


maxcost = 0
for kit in kits(items):
    if not play({'boss': boss.copy(), 'me': stats(kit)}):
        maxcost = max(stat(kit, 'Cost'), maxcost)

print("Part2", maxcost)
