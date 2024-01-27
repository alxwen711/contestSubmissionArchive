import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
goal is to split into 2 subsequences (not contiguous) that
are as close to decreasing (equal inclusive) as possible
does greedy work? WA on pretest 2 -> probably not
track dp states?
"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    av = 99999999999999
    bv = 99999999999999
    for i in range(n):
        x = ar[i]
        if av >= x: av = x
        elif bv >= x: bv = x
        else:
            ans += 1
            if av < bv: av = x
            else: bv = x
        if av > bv: av,bv = bv,av
    print(ans)
