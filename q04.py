from hashlib import md5

key = 'iwrupvqb'

i = 0
hash = ''
while hash != '00000':
    i += 1
    inp = key + str(i)
    hash = md5(inp.encode()).hexdigest()[0:5]

print(i)

i = 0
hash = ''
while hash != '000000':
    i += 1
    inp = key + str(i)
    hash = md5(inp.encode()).hexdigest()[0:6]

print(i)
