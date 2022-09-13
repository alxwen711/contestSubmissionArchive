import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def bfunc(x, ar = None) -> bool:
    for k in range(x):
        if (ar[k] + ar[-k-1]) < 0: return False
    return True

def bsearch(low, high, ar = None):
    while high - low > 1:
        mid = (low+high)//2 
        if bfunc(mid,ar[:2*mid]): low = mid
        else: high = mid

    #diff is small enough
    if bfunc(high,ar[:2*high]): return high
    else: return low

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    cr = list()
    for j in range(n):
        cr.append(br[j]-ar[j])
    cr.sort()
    cr.reverse()
    print(bsearch(0,n//2,cr))
    
