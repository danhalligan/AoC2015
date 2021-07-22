import re

dat = open("inputs/q05.txt", "r").read().split()

# part 1
def nice(x):
    return len(re.findall('[aeiou]', x)) >= 3 and \
        len(re.findall(r'(\w)\1', x)) >= 1 and \
        len(re.findall('(ab|cd|pq|xy)', x)) == 0
    
print("Part1:", list(map(nice, dat)).count(True))



# part 2
def nice(x):
    return len(re.findall(r'(\w\w).*\1', x)) >= 1 and \
        len(re.findall(r'(\w).\1', x)) >= 1
        
print("Part2:", list(map(nice, dat)).count(True))
