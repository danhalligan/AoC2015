from numba import jit
import re

inp = [int(x) for x in re.findall(r"\d+", open("inputs/q25.txt").read())]

@jit(nopython=True)
def part1(x, y, n):
    i, j = 1, 1
    while i < 10000:
        if i == x and j == y: return n
        n = n * 252533 % 33554393
        if i == 1:
            i, j = j + 1, 1
        else:
            i, j = i-1, j+1

print("Part1:", part1(inp[0], inp[1], 20151125))
