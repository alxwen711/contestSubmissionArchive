import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if your product exceeds a certain point, then it's probably best to
just take the product of everything (excluding 1's)
alternatively, if there are under 20ish values that are not 1
2**20 is about 1 million
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    cr = list()
    s = [0] #sum array
    for j in range(n):
        s.append(s[-1]+ar[j])
        if ar[j] != 1:
            br.append(j)
            cr.append(ar[j])
    m = len(br)
    if m <= 1: print(1,1) #no mult
    elif m >= 20: print(br[0]+1,br[-1]+1) #full mult (strip 1s)
    else: #figure out answer
        best = -1
        ansa,ansb = -1,-1
        for a in range(m-1):
            base = cr[a]
            for b in range(a+1,m):
                base *= cr[b]
                val = base+s[n]-s[br[b]+1]+s[br[a]]
                if val > best:
                    best = val
                    ansa = br[a]+1
                    ansb = br[b]+1
        if best >= s[n]: print(ansa,ansb)
        else: print(1,1)
