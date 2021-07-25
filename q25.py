import numpy as np

n = 20151125
i, j = 1, 1

while i < 10000:
    if i == 2981 and j == 3075: break
    n = n * 252533 % 33554393
    if i == 1:
        i, j = j + 1, 1
    else:
        i, j = i-1, j+1

print("Part1:", n)
