import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = list()
    x = n//2
    for j in range(x):
        ar.append(x+j+1)
        ar.append(j+1)
    if n % 2 == 1: ar.append(n)
    print(*ar)
