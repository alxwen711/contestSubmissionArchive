import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    a,b,c = readints()
    n = a+b+c
    if n % 2 == 1: print(-1)
    elif max(a,b,c) > n//2: print(n-max(a,b,c))
    else: print(n//2)
