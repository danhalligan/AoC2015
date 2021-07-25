import game
import importlib
from copy import deepcopy

def read_boss():
    boss = open("inputs/q22.txt", "r").read().splitlines()
    boss = dict(x.split(": ") for x in boss)
    for d in boss: boss[d] = int(boss[d])
    return boss

# Recursively play games as a bedth-first search.
# We prune (or return False) any branches where the spend is over the current best
def play(x):
    if x.player['Spend'] > best: return False, 10000000
    for spell in x.castable():
        y = deepcopy(x)
        result, spend = y.round('player', spell=spell)
        if result is None: result, spend = y.round('boss')
        if result is None: yield from play(y)
        if result: yield spend


# For results of each game, record if we've improved.
def find_best(x):
    global best
    for tmp in play(x):
        if tmp < best:
            best = tmp
            print(best)


x = game.Game(
    player = {'Hit Points': 50, 'Mana': 500, 'Armor': 0, 'Spend': 0},
    boss = read_boss()
)
best = 10000000
find_best(x)
print("Part1:", best)

x = game.Game(
    player = {'Hit Points': 50, 'Mana': 500, 'Armor': 0, 'Spend': 0},
    boss = read_boss(),
    hard = True
)
best = 10000000
find_best(x)
print("Part2:", best)
