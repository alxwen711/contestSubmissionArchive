import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
5 8 10
7 11 13
"""
for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    low = list()
    high = list()
    a,b = 0,0
    while a != n:
        if ar[a] <= br[b]:
            low.append(br[b]-ar[a])
            a += 1
        else: b += 1
    a,b = -1,-1
    flag = False
    while a != -n-1:
        high.append(br[b]-ar[a])
        if a != -n:
            if ar[a] > br[a-1]: b = a-1
        a -= 1
    high.reverse()
    print(*low)
    print(*high)
