import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    if n == 1: return 0
    x = min(ar)
    ans = 0
    for i in range(n):
        if ar[i] >= (2*x):
            y = (ar[i]-1) // (2*x-1)
            ans += y
        
    return ans

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
