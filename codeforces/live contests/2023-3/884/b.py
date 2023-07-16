import sys
 
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
 
from math import sqrt, floor
 
def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    return ar
 
"""
mex -> smallest POSITIVE not included
mex = 2 -> 1 is present
mex = 3 -> 1-2 is present
mex = 13 -> 1-12 is present
attempt to center the 1
maximize 2 setups, 3 setups, 5 setups, etc.
1,1-2,1-4,1-6
"""
 
 
s = sieve(200004)
 
 
for i in range(readint()):
    n = readint()
    if n == 1: print("1")
    elif n == 2: print("2 1")
    elif n == 3: print("2 1 3")
    elif n == 4: print("2 1 4 3")
    else:
        d = {}
        d[0] = [2,1,4,3] 
        maxt = 0
        mint = 0
        lv = 1
        rv = 2
        br = list()
        left = False
        for j in range(5,n+1):
            br.append(j)
            if s[j+1]: #append
                nv = len(br)
                if lv < rv: #throw to left side
                    lv += nv
                    mint -= 1
                    d[mint] = br
                    br = list()
                    left = True
                else: #throw to right side
                    br.reverse()
                    rv += nv
                    maxt += 1
                    d[maxt] = br
                    br = list()
                    left = False
        #br.reverse()
        for snth in br:
            if lv < rv:
                lv += 1
                mint -= 1 
                d[mint] = [snth]
            else:
                rv += 1
                maxt += 1
                d[maxt] = [snth]
        ans = list()
        #print(d)
        for ii in range(mint,maxt+1):
            for jj in d[ii]:
                ans.append(jj)
        print(*ans)
