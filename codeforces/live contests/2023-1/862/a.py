import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    x = 0
    for j in range(n):
        x = x ^ ar[j]
    if n % 2 == 1: print(x)
    elif x == 0: print(0)
    else: print(-1)
