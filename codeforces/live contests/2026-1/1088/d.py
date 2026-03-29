import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
number of times a bit shows up
subsequences thus order does not matter

start constructing from the last value
22 24 10 1 0
0 0 0 0 0 (0) subtract is now 0
1 1 1 1 0 (1-0*5 = 1) subtract is now 0+1
7 7 7 1 0 (10-1*4-0*10 = 6) subtract is now 0+4+6
7 7 7 1 0 (24-6*3-1*6-0*10 = 0) subtract is now 0+6+18
7 7 7 1 0 (22-0*2-6*3-1*4-0*5 = 0) subtract is now 0+4+18+0 

there are only about 30 or so bits that can be added, so most of these
will evaluate to 0?
"""

m = 1000000007
facts = [1]
invs = [1]

for i in range(1,110000):
    facts.append((facts[-1]*i) % m)
    invs.append(pow(facts[-1],m-2,m))

for _ in range(readint()):
    n = readint()
    ar = readar()
    v = 0
    ans = [0]*n
    decrements = list()
    for j in range(n-1,-1,-1):
        r = ar[j]
        for d in decrements:
            # update all decrements here
            dist = d[1]-j-1
            # d[1] choose (j+1)
            r = (r-((d[0]*facts[d[1]]*invs[j+1]*invs[dist]) % m)) % m
        if r != 0:
            v += r
            decrements.append([r,j+1]) # val,index base?
        ans[j] = v
        #print(decrements)
    print(*ans)
