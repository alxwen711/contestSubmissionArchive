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

ref = sieve(1000000)

def solve(n,m,ref):
    ans = list()
    for i in range(n):
        tmp = [0]*m
        ans.append(tmp)
    if not ref[n]: #fill by columns
        v = 1
        for a in range(m):
            for b in range(n):
                ans[b][a] = v
                v += 1
    elif not ref[m]: #fill by rows
        v = 1
        for a in range(n):
            for b in range(m):
                ans[a][b] = v
                v += 1
    else:
        rf = list() #row fill order
        xx = n//2
        for s in range(n//2):
            rf.append(xx-s-1)
            rf.append(xx+s+1)
        rf.append(xx)
        v = 1
        for a in range(n):
            for b in range(m):
                ans[rf[a]][b] = v
                v += 1
    for aa in range(n):
        print(*ans[aa])
    
        
for i in range(readint()):
    n,m = readints()
    solve(n,m,ref)    
