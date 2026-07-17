import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,a,b):
    if a + b < (n-1): return "Yes"
    if a == n or b == n:
        if a == n and b == n: return "Yes"
        return "No"
    return "No"

for i in range(readint()):
    n,a,b = readints()
    print(solve(n,a,b))
