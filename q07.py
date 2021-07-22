import re
import functools

class smart_dict(dict):
    def __missing__(self, key):
        return lambda: int(key)

@functools.cache
def binfn(a, b, op):
    if op == 'AND':
        o = circuit[a]() & circuit[b]()
    elif op == 'OR':
        o = circuit[a]() | circuit[b]()
    elif op == 'LSHIFT':
        o = circuit[a]() << int(b)
    elif op == 'RSHIFT':
        o = circuit[a]() >> int(b)
    return(o)


circuit = smart_dict()
dat = open("inputs/q07.txt", "r").read().splitlines()

for x in dat:
    s = x.split(' -> ')
    op = s[0]
    to = s[1]
    if re.match(r'^\w+$', op):
        fn = lambda v=op: circuit[v]()
    elif (o := re.match(r'^(.+)\s(AND|OR|LSHIFT|RSHIFT)\s(.+)$', op)):
        fn = lambda a=o.group(1), b=o.group(3), op=o.group(2): binfn(a, b, op)
    elif (o := re.match(r'NOT\s(.+)$', op)):
        fn = lambda a=o.group(1): int(65535 - circuit[a]())
    circuit[to] = fn


print("Part1:", circuit['a']())

binfn.cache_clear()
circuit['b'] = lambda: 3176
print("Part2:", circuit['a']())

