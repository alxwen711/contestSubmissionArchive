import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
r is at least 3 and l is at most 2n-1 unless no swaps are required
anything in wrong position serves as lower limit for l

if n is misplaced, r has to be at least n+1
if 1 is misplaced, l has to be at most n+1

any misplaced values must be swapped at least once
we can always fix one value at a time, but the last two values
must be fixed at the same time

feels like some sort of way that given a minimum, compute required maximum
"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    for i in range(n):
        if ar[i] != i+1: br.append(ar[i])
    br.sort()
    if len(br) == 0: print((n)*(2*n+1))
    elif ar == [2,1]: print(6)
    else:
        mi = br[0]+n # min is at most this
        ma = 1+br[-1] # max is at least this
        # just assume range needs to be at least 1 value? (first example fails)
        ans = 0
        for i in range(1,mi+1):
            maa = max(i+1,ma)
            if maa <= 2*n: ans += 2*n-maa+1
        if len(br) == 2: ans += 1
        print(ans)
