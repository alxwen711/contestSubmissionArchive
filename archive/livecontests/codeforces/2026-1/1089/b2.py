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
    d = [0]*n # track game end potential
    for i in range(n):
        if ar[i] > (i+1): d[i] = ar[i]-1 # game ends upon reaching this index
        else: d[i] = n
    #print(d)
    # now for each index, determine how many have a higher value
    h = [0]*(n+1)
    ans = 0
    c = 0
    for j in range(n):
        if d[j] > j:
            c += 1
            h[d[j]] += 1
        ans = max(c,ans)
        c -= h[j+1]
    print(ans)
