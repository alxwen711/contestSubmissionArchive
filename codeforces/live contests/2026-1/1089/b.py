import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
add back in in reverse order?

two types of seats, those that end
the game prematurely, and those that are
unconditional
for game ending seats, keep running sum of how many values are lower
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    d = [0]*(n+1) # seat to pos
    for i in range(n):
        d[ar[i]] = i
    h = [0]*n
    c = 0
    ans = 0
    print(d)
    for j in range(1,n+1):
        if d[j] < j:
            c += 1
            h[d[j]] = 1
        ans = max(ans,c)
        c -= h[j-1]
    print(ans)
