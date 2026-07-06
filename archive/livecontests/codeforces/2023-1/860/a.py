import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar,br):
    low = min(ar[-1],br[-1])
    high = max(ar[-1],br[-1])
    for i in range(n-1):
        l,h = min(ar[i],br[i]),max(ar[i],br[i])
        if h > high or l > low: return "No"
    return "Yes"

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(solve(n,ar,br))
