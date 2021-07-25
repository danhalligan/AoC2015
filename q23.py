import re

def run(program, reg = {'a': 0, 'b': 0}):
    pos = 0
    while True:
        if pos >= len(program): break
        inst = program[pos]
        if inst[0] == 'hlf':
            reg[inst[1]] /= 2
            pos += 1
        elif inst[0] == 'tpl':
            reg[inst[1]] *= 3
            pos += 1
        elif inst[0] == 'inc':
            reg[inst[1]] += 1
            pos += 1
        elif inst[0] == 'jmp':
            pos += int(inst[1])
        elif inst[0] == 'jie':
            if reg[inst[1]] % 2 == 0: pos += int(inst[2])
            else: pos += 1
        elif inst[0] == 'jio':
            if reg[inst[1]] == 1: pos += int(inst[2])
            else: pos += 1
    return reg


program = open('inputs/q23.txt').read().splitlines()
program = [re.split(r',*\s+', x) for x in program]

print("Part1:", run(program)['b'])
print("Part2:", run(program, {'a': 1, 'b': 0})['b'])
