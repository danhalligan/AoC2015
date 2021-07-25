from itertools import product

def fill(jars, vol):
    for i in range(len(jars)):
        remainder = vol-jars[i]
        if remainder > 0:
            for a, b in product([jars[i]], fill(jars[i+1:], remainder)):
                yield [a] + b
        elif remainder == 0:
            yield [jars[i]]


dat = [20, 15, 10, 5, 5]
list(fill(dat, 25))

dat = [int(x) for x in open("inputs/q17.txt", "r").read().split()]
results = list(fill(dat, 150))

print("Part1:", len(results))

target = min([len(x) for x in results])
print("Part2:", len([x for x in results if len(x) == target]))
