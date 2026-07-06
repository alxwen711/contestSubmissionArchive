import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar,br):
    h = [1]*(n+1)
    h[0] = 0
    for j in range(n):
        if ar[j] > br[j]: #otherwise mono always finishes first
            """
            all n where (ar[j]-1)//n > (br[j]-1)//n fail
            br[j],br[j]+1...ar[j]-1, find all factors of values, all fail
            each has at most 160 factors
            use segment tree to group set a range of values' factors???
            """


    return h

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    x = solve(n,ar,br)
    ans = list()
    for k in range(n+1):
        if x[j] == 1: ans.append(k)
    print(len(ans))
    print(*ans)
