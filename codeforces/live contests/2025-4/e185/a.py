import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    if n == 1: print(1)
    elif n == 2: print(9)
    elif n == 3: print(29)
    elif n == 4: print(56)
    elif n == 5: print(95)
    else: print(5*(n*n-n-1))
