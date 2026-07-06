import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
blatantly states O(n^2) might be a solution
ANYTHING above 2 should be 0

first round, get all possible values
"""

def bsearch(ar,x):
    low = 0
    high = len(ar)-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] == x: return 0
        elif ar[mid] > x: high = mid
        else: low = mid
    return min(abs(ar[low]-x),abs(ar[high]-x))

def solve(n,k,ar):
    if k == 1: #can brute force
        ans = min(ar)
        for a in range(n-1):
            for b in range(a+1,n):
                ans = min(ans,abs(ar[a]-ar[b]))
        return ans
    elif k == 2: #bit harder
        br = list()
        for a in range(n-1):
            for b in range(a+1,n):
                br.append(abs(ar[a]-ar[b]))
        br.sort()
        #print(br)
        ans = min(ar)
        ans = min(ans,br[0])
        for c in ar:
            ans = min(ans,bsearch(br,c))
        return ans
    else: return 0
    
for _ in range(readint()):
    n,k = readints()
    ar = readar()
    print(solve(n,k,ar))
