import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
once a value is 49+, any multiplier increase equals/exceeds
a plus diff, solution is then to take highest multiplier cases
past that, idk

only have to keep the ten highest multipliers
and ten highest increments?

20 choose 10 is viable, how to check for optimal given multipliers

using dp tracker gives C(20,10)*(C(10,1 to 10)) -> about 190 million

there should be something better???

depending on how fast br sums to 50, could remove several? (not consistent)
"""

n,k = readints()
ar = list()
br = list()
for i in range(n):
    a,b = readints()
    ar.append((-a,-b,i,a,b))
    br.append((-b,i,a,b))
ar.sort()
br.sort()
ar = ar[:k]
br = br[:k]

# only tuples left in ar/br need to be considered
