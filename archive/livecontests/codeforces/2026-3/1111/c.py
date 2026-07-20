import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
feels very likely this is 0/1/2/-1
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    a,b,c,d = 0,0,0,0
    for i in range(n):
        if ar[i] == 0 and br[i] == 1: a += 1
        if ar[i] == 1 and br[i] == 0: b += 1
        if ar[i] == 1 and br[i] == 1: c += 1
        if ar[i] == 0 and br[i] == 0: d += 1
    if a == 0 and b == 0: print(0)
    elif b % 2 == 1: print(1)
    elif b == 0:
        # some backwards moves are needed
        if c != 0 and d != 0: print(2)
        else: print(-1)
    else: print(2)
