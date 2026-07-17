import sys
from math import floor,sqrt,ceil
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
Using help from first two hints, maximum sum value has to be 2n
so min between ai and aj is at most floor(sqrt(2n))
for each element, if a val is not overlimit,
"""

def solve(n,ar,br):
    d = [0]*(n+1)
    #for i in range(n+1):
    #    tmp = {}
    #    d.append(tmp)
    limit = floor(sqrt(2*n))
    h = [0]*(n+1)
    for j in range(n):
        a,b = ar[j],br[j]
        if d[a] == 0: d[a] = {}
        if d[a].get(b) == None: d[a][b] = 0
        d[a][b] += 1
        h[a] = 1
    ans = 0
    cr = list()
    for ss in range(limit+1):
        if h[ss] == 1:
            cr.append(ss)
    ccc = len(cr)
    for s in range(limit+1,n+1):
        if h[s] == 1:
            cr.append(s)
    c = len(cr)
    for kk in range(ccc):
        k = cr[kk]
        dup = 0
        for ll in range(kk,c):
            l = cr[ll]
            x = k*l
            if x > 2*n: break
            for m in d[l].keys():
                freq = d[l][m]
                if x-m in d[k]:
                    if k == l: #overcount
                        if m+m == x: #same key
                            ans += (freq*freq-freq)//2
                        else: #prevent double count in form (x,a),(x,b)
                            dup += (d[k][x-m]*freq)
                    else: 
                        ans += d[k][x-m]*freq
        dup //= 2
        ans += dup
    return ans
            

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(solve(n,ar,br))

