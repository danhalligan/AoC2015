import re
import json

dat = open('inputs/q12.txt').read()
print("Part1", sum([int(x) for x in re.findall(r'-*\d+', dat)]))

def count_ints(x):
    if (isinstance(x, list)):
        return sum(count_ints(e) for e in x)
    elif (isinstance(x, dict) and not "red" in x.values()):
        return count_ints(list(x.values()))
    elif (isinstance(x, int)):
        return(x)
    else: 
        return(0)


print("Part2", count_ints(json.loads(dat)))
