import numpy as np
import re

dat = open("inputs/q06.txt", "r").read().splitlines()

lights = np.zeros(shape = (1000,1000))

for x in dat:
    coords = re.findall(r'\d+,\d+', x)
    c1 = [int(i) for i in coords[0].split(',')]
    c2 = [int(i) for i in coords[1].split(',')]
    
    if re.match('turn on', x):
        action = lambda x: 1
    elif re.match('turn off', x):
        action = lambda x: 0   
    else:
        action = lambda x: 1 if x == 0 else 0

    for i in range(c1[0], c2[0]+1):
        for j in range(c1[1], c2[1]+1):
            lights[i,j] = action(lights[i,j])

int(sum(sum(lights)))


lights = np.zeros(shape = (1000,1000))

for x in dat:
    coords = re.findall(r'\d+,\d+', x)
    c1 = [int(i) for i in coords[0].split(',')]
    c2 = [int(i) for i in coords[1].split(',')]
    
    if re.match('turn on', x):
        action = lambda x: x + 1  
    elif re.match('turn off', x):
        action = lambda x: x - 1 if x > 0 else 0
    else:
        action = lambda x: x + 2
        
    for i in range(c1[0], c2[0]+1):
        for j in range(c1[1], c2[1]+1):
            lights[i,j] = action(lights[i,j])


int(sum(sum(lights)))

