
dat = open("inputs/q08.txt", "r").read().splitlines()

# part 1 
parsed = list(map(lambda x: bytes(x[1:-1], "utf-8").decode('unicode-escape'), dat))
sum(map(len, dat)) - sum(map(len, parsed))

# part 1 v2
sum(map(lambda x: len(x) - len(eval(x)), dat))

# part 2
[2 + s.count('\\') + s.count('"') for s in dat[0:10]]
