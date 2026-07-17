import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
1 1 2 2 3 3 4 4 -> ?

something with repeating the values is more efficient
powers of 3 increase faster than powers of 2 (closer to e)

doing weird insertions (negative) acts like adding powers of 2
if a segment is left at the end, then use incrementing logic
can insert multiple negatives between two positives
"""
def solve(n):
    n -= 1
    e = 1
    v = 1
    ar = list()
    ar.append((1,0))
    while (v*2+1) <= n:
        v = v*2+1
        e += 1
        ar.append((e,0))
    e = 0
    n -= v
    v += 1
    while n != 0:
        if v <= n:
            n -= v
            ar.append((e,1))
        else:
            e += 1
            v //= 2
    ar.sort()
    #print(ar)
    a,b = -1,1
    ans = list()
    for x in range(len(ar)):
        if ar[x][1] == 1:
            ans.append(a)
            a -= 1
        else:
            ans.append(b)
            b += 1
    print(len(ans))
    print(*ans)


    
for _ in range(readint()):
    solve(readint())
