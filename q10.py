def look_and_say(inp):
    x = inp[0]
    tot = 0
    new = ''
    for c in inp:
        if c != x:
            new += str(tot) + x
            x = c
            tot = 0
        tot += 1
    new += str(tot) + str(x)
    return(new)


def repeat(x, n):
    for i in range(n):
        x = look_and_say(x)
    print(len(x))

repeat('1113222113', 40)
repeat('1113222113', 50)
