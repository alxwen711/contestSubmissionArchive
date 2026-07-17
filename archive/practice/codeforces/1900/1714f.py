import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 to 2 has distance a
2 to 3 has distance b
3 to 1 has distance c
"""

def solve(n,a,b,c):
    if a > (b+c):
        print("NO")
        return
    d = b+c-a
    if d % 2 == 1:
        print("NO")
        return
    nr = a+1+(d//2)
    lo = b-(d//2)
    ro = c-(d//2)
    if nr > n or min(lo,ro) < 0:
        print("NO")
        return
    print("YES")
    if d == 0: # build chain
        h = [0]*n
        h[0] = 1
        h[a] = 2
        crit = c
        v = 4
        for i in range(n):
            if i == crit: h[i] = 3
            elif h[i] == 0:
                h[i] = v
                v += 1
        for j in range(n-1):
            print(h[j],h[j+1])
            
    else: # fill 1-2 chain and extend
        prev = 1
        for g in range(a-1):
            nv = 4+g
            print(prev,nv)
            prev = nv
        print(prev,2)
        v = prev+1 #track value to add
        if a == 1: v = 4
        if ro == 0: prev = 1
        elif ro == a: prev = 2
        else: prev = 3 + ro
        for kk in range(d//2-1):
            print(prev,v)
            prev = v
            v += 1
        print(prev,3)
        prev = 3
        while v <= n:
            print(prev,v)
            prev = v
            v += 1

for i in range(readint()):
    n,a,b,c = readints()
    solve(n,a,b,c)
