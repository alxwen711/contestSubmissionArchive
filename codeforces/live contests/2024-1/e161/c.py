import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
pre compute l to r and r to l distances
"""


def solve():
    n = readint()
    ar = readar()
    lr = [0]*n
    rl = [0]*n
    lr[1] = 1
    rl[n-2] = 1
    for i in range(2,n):
        if abs(ar[i]-ar[i-1]) < abs(ar[i-1]-ar[i-2]): lr[i] = lr[i-1]+1
        else: lr[i] = lr[i-1]+abs(ar[i]-ar[i-1])

    for j in range(n-3,-1,-1):
        if abs(ar[j]-ar[j+1]) < abs(ar[j+1]-ar[j+2]): rl[j] = rl[j+1]+1
        else: rl[j] = rl[j+1]+abs(ar[j]-ar[j+1])

    m = readint()
    for _ in range(m):
        x,y = readints()
        x -= 1
        y -= 1
        if x < y: print(lr[y]-lr[x])
        else: print(rl[y]-rl[x])

for _ in range(readint()):
    solve()
