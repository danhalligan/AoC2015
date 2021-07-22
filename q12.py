import re
import json

sum([int(x) for x in re.findall(r'-*\d+',open('inputs/q12.txt').read())])

def count_ints(x):
    if (isinstance(x, list)):
        return sum(count_ints(e) for e in x)
    elif (isinstance(x, dict) and not "red" in x.values()):
        return count_ints(list(x.values()))
    elif (isinstance(x, int)):
        return(x)
    else: 
        return(0)


dat = json.loads(open('inputs/q12.txt').read())
count_ints(dat)
