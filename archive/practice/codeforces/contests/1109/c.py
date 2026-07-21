import sys
from math import gcd

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,x,y = readints()
    ar = readar()
    g = gcd(x,y)
    if g == 1: print("YES")
    else:
        ans = "YES"
        for i in range(g):
            d = {}
            for u in range(i,n,g):
                d[ar[u]] = 1
            for v in range(i+1,n+1,g):
                if d.get(v) == None:
                    ans = "NO"
                    break
            if ans == "NO": break
        print(ans)
