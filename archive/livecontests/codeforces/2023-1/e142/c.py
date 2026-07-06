import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def test(n,ar,x):
    l = n - (2*x)
    if l <= 1: return True
    st,ed = 1+x,n-x
    for i in range(n):
        v = ar[i]
        if st <= v <= ed:
            if v == st: st += 1
            else: return False
    return True

def bsearch(n,ar):
    low = 0
    high = n//2
    while high-low > 1:
        mid = (low+high)//2
        if test(n,ar,mid): high = mid
        else: low = mid
    if test(n,ar,low): return low
    return high


for i in range(readint()):
    n = readint()
    ar = readar()
    print(bsearch(n,ar))
