import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
vals cap at 1000
bob always takes highest x to flip
"""

for _ in range(readint()):
    n,k,x = readints()
    ar = readar()
    ar.sort()
    ar.reverse()
    s = sum(ar)
    sub = sum(ar[:x])
    ans = s-sub-sub
    for i in range(k):
        s -= ar[i]
        sub -= ar[i]
        if (i+x) < n: sub += ar[i+x]
        ans = max(ans,s-sub-sub)
    print(ans)
