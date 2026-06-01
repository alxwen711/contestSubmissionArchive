import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
C1 is O(n^2)
C2 is O(n log n)

x tables with m seats each
I -> must be alone at table (until they aren't)
E -> not I
A -> anything is fine

ternary search? A -> basically put them at their own tables
have some number of isolation tables

2 seats per table -> all odds subtract 1
3+ seats per table -> as long as it's not 1
"""

def f(s,x,m,i):
    # set i tables to iso
    a,b = i,(x-i)*m
    bcount = 0
    ans = 0
    for p in s:
        if p == "I":
            if a != 0:
                ans += 1
                a -= 1
        elif p == "E":
            if b != 0:
                ans += 1
                b -= 1
                bcount += 1
        else:
            if b != 0:
                ans += 1
                b -= 1
                bcount += 1
            elif a != 0:
                ans += 1
                a -= 1
    # double check that bcount makes sense
    if m == 2:
        if bcount % 2 == 1: ans -= 1
    else:
        if bcount == 1: ans -= 1
    return ans
    
for _ in range(readint()):
    n,x,m = readints()
    s = readin()
    if m == 1:
        print(max(x,n-s.count("E")))
    else:
        ans = 0
        for i in range(x+1):
            ans = max(ans,f(s,x,m,i))
            print(i,f(s,x,m,i))
        print(ans)
