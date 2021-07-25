import numpy as np
import re

def adj(i, d):
    return range(max(i-1, 0), min(i+2, d))

def neighbours(i, j, d):
    for x in adj(i, d):
        for y in adj(j, d):
            if x == i and y == j: continue
            yield [x, y]

def update(x):
    y = np.copy(x)
    d = len(x)
    for i in range(d):
        for j in range(d):
            state = dat[i,j]
            tot = sum(dat[x, y] for x, y in neighbours(i, j, d))
            if state == 1 and tot not in [2, 3]:
                y[i, j] = 0
            if state == 0 and tot == 3:
                y[i, j] = 1
    return y

def printgrid(mat):
    for line in mat:
        print(*['#' if x else '.' for x in line], sep='')

def read(file):
    dat = open(file, "r").read().splitlines()
    return np.array([[1 if x == "#" else 0 for x in line] for line in dat])

dat = read("inputs/q18-test.txt")
for i in range(4):
    dat = update(dat)

sum(sum(dat))


dat = read("inputs/q18.txt")
for i in range(100):
    dat = update(dat)

print("Part1:", sum(sum(dat)))


def always_on(x):
    d = len(x) - 1
    x[0,0] = 1
    x[0,d] = 1
    x[d,0] = 1
    x[d,d] = 1

dat = read("inputs/q18.txt")
always_on(dat)
for i in range(100):
    dat = update(dat)
    always_on(dat)

print("Part2:", sum(sum(dat)))
