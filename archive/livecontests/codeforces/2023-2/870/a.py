import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    for j in range(1,n):
        if ar[n-j] > j and ar[n-j-1] <= j: return j
    if ar[-1] == 0: return 0
    return -1

for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    print(solve(n,ar))
