import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def solve(n,ar):
    for a in range(n-1):
        if ar[a] == 1: ar[a] += 1
    for i in range(n-1):
        if ar[i+1] % ar[i] == 0:
            ar[i+1] += 1
    print(*ar)
    

for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
