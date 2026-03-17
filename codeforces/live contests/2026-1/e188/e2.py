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
    while x != 0:
        v += x % 10
        x //= 10
    return v

chain = [digitsum(i) for i in range(900000)]
exact = [i for i in range(900000)]
req = [[0,0,0,0,0,0,0,0,0,0]] # 0 case should not happen

def movedown(i):
    x = i
    t = 0
    while x >= 10:
        t += x
        x = digitsum(x)
    if x != 0:
        t += x
        t += x
    return t
        
for j in range(1,900000):
    exact[j] = movedown(j)
    
d = {}
for u in range(900000):
    if d.get(exact[u]) == None: d[exact[u]] = list()
    d[exact[u]].append(u)

for _ in range(readint()):
    s = readin()
    if len(s) == 1:
        print(s)
        continue
    h = [0]*10
    t = 0
    for i in s:
        x = int(i)
        h[x] += 1
        t += x
    for l in d[t]:
        subset = [0]*10
        cs = [l]
        while cs[-1] >= 10:
            cs.append(chain[cs[-1]])
        for u in cs:
            vv = u
            while vv != 0:
                subset[vv%10] += 1
                vv //= 10
        flag = True
        for snth in range(10):
            if subset[snth] > h[snth]:
                flag = False
                break
        if flag: # solution exists
            ans = list()
            for why in range(9,-1,-1):
                ans.append(str(why)*(h[why]-subset[why]))
            for uu in cs:
                ans.append(str(uu))
            print("".join(ans))
            break
