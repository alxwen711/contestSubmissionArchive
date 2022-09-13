import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = list()
    if n == 1: print("1")
    else:
        ar.append(n)
        for j in range(1,n):
            ar.append(j)
        print(*ar,"\n")
