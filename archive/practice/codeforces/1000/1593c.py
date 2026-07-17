import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def bfunc(x: int, ar: list[int], n: int) -> bool:
    cat = 0
    k = len(ar)
    st = k-x
    for i in range(x):
        #print(cat)
        if cat >= ar[st+i]: return False
        dist = n-ar[st+i]
        cat += dist
    return True


def bsearch(low: int, high: int, ar: list[int], n: int) -> int:
    while high - low > 1:
        mid = (low+high)//2
        if bfunc(mid,ar,n): low = mid
        else: high = mid

    #diff between high and low is 1 (or 0)
    if bfunc(high,ar,n): return high
    else: return low

for i in range(readint()):
    n,k = readints()
    ar = readar()
    ar.sort()
    print(bsearch(1,k,ar,n))
