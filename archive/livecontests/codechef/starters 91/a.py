import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    if n % 2 == 1: print(-1) #n//2+1 element gcd = 1, impossible
    else:
        ar = list()
        for j in range(n):
            ar.append(j+1)
        ar.reverse()
        print(*ar)
