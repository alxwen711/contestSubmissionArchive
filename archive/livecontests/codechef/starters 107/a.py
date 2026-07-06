import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    ar = list()
    for i in range(n,0,-1):
        ar.append(i)
    print(*ar)
