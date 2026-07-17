import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar,br):
    #cr = list()
    m = max(ar)
    for j in range(n):
        if ar[j] > br[j]: return "NO"
        #cr.append(max(br[j]-m,0))
        if j == n-1:
            if br[-1]-br[0] > 1 and br[-1] != ar[-1]: return "NO"
        else:
            if br[j]-br[j+1] > 1 and ar[j] != br[j]: return "NO"
    return "YES"

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(solve(n,ar,br))
