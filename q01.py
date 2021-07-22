dat = list(open("inputs/q01.txt", "r").read())

print("Part1:", dat.count('(') - dat.count(')'))

i, tot = 0, 0
while tot != -1:
    tot += {'(': 1, ')': -1}[dat[i]]
    i += 1

print("Part2:", i)
