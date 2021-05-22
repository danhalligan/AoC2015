from collections import defaultdict

dat = list(open("input.txt", "r").read())

# part 1
map = defaultdict(lambda: 0)
i, j = 0, 0
map[i,j] = 1
for p in dat:
    i += {'^': 0, '>': 1, 'v': 0, '<': -1}[p]
    j += {'^': 1, '>': 0, 'v': -1, '<': 0}[p]
    map[i,j] += 1

print(len(map.keys()))


# part 2
map = defaultdict(lambda: 0)
i1, j1 = 0, 0
i2, j2 = 0, 0

map[i1,j1] = 2
turn = 0
for p in dat:
    i = {'^': 0, '>': 1, 'v': 0, '<': -1}[p]
    j = {'^': 1, '>': 0, 'v': -1, '<': 0}[p]
    if turn % 2  == 0:
        i1 += i
        j1 += j
        map[i1, j1] += 1
    else:
        i2 += i
        j2 += j
        map[i2, j2] += 1
    turn += 1

print(len(map.keys()))
