import sys
from math import ceil
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def test(x,mid):
    return mid*mid >= x

def sqrt(x):
    low = 1
    high = x
    while high-low > 1:
        mid = (low+high)//2
        if test(x,mid): high = mid
        else: low = mid
    if test(x,low): return low
    else: return high

for i in range(readint()):
    n = readint()
    x = sqrt(n)
    print(x-1)
    
