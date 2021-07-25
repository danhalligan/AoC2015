# Not a very satisfactory answer.

# I search through colossally numbers (CAN, which should get very high scores
# and find the minimum CAN that is not above the target from here I go up in
# units of the previous CAN This is not guaranteed to work though.

# The first answer is a superabundant number: https://oeis.org/A004394. The
# second is not, but it does have 189 divisors!

# superabundant numbers
sa = [2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720, 1441440]
target = 29000000

# 10 + 20 (if multiple of 2) + 30 (if multiple of 3) etc.
def presents(n):
    return sum(i*10 for i in range(1, n+1) if n % i == 0)
  
def search(fn):
    x = [fn(x) > target for x in sa]
    i = x.index(True)
    for i in range(sa[i-1], sa[i], sa[i-2]):
        if fn(i) > target: return i

print("Part1:", search(presents))

def presents2(n):
    return sum(i*11 for i in range(1, n+1) if n % i == 0 and n/i <= 50)

print("Part2:", search(presents2))
