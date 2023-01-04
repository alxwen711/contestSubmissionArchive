import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = list()
    if n % 2 == 1:
        ar.append(n)
        n -= 1
        for j in range(n//2):
            ar.append(j+1)
            ar.append(n-j)
    else:
        for j in range(n//2):
            ar.append(n-j)
            ar.append(j+1)
    print(*ar)
