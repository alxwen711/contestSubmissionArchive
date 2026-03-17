import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
it is always possible to rearrange the digits to the constraints
process ends if x <= 9, math solution?

max sum of digits is 900000
max of this iteration is 899999 -> 53
third max is 49 -> 13 -> 4
4 <- 13 <- 49 <- 888889 <- ???

method: brute force the chains, something has to work

try building a base 53 chain
if this fails, isolate 1 val, check for sum match and subset
if this fails,

actually what if just make dictionary setup up to 899999?
then conditions are to check for digit sum match and subset rule
"""

def digitsum(i):
    v = 0
    x = i
    okay = [0]*10
    while x != 0:
        v += x % 10
        okay[x % 10] += 1
        x //= 10
    return v,okay

chain = [digitsum(i)[0] for i in range(900000)]
exact = [i for i in range(900000)]
req = [[0,0,0,0,0,0,0,0,0,0]] # 0 case should not happen

def movedown(i):
    ar = [0]*10
    x = i
    t = 0
    while x >= 10:
        t += x
        v,br = digitsum(x)
        x = v
        for snth in range(10):
            ar[snth] += br[snth]
    if x != 0:
        t += x
        ar[x] += 1
    return t,ar
        
for j in range(1,900000):
    v,reqset = movedown(j)
    exact[j] = v
    req.append(reqset)

d = {}
for u in range(900000):
    if d.get(exact[u]) == None: d[exact[u]] = list()
    d[exact[u]].append(u)

"""
for _ in range(readint()):
    s = readin()
    h = [0]*10
    t = 0
    for i in s:
        x = int(i)
        h[x] += 1
        t += x
        
"""
