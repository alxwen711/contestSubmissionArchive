import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
x and y are limited to be at most k
binary search?

x//y = a, x % y = b
min setup is:
y = b + 1
x = (a+1)*(b+1)-1
"""

def f(ar,br,x,k):
    for i in range(x):
        a = ar[i]
        b = br[x-i-1]
        if (a+1)*(b+1)-1 > k: return False
    return True

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    ar.sort()
    br.sort()
    low = 1
    high = n
    while high-low > 1:
        mid = (low+high)//2
        if f(ar,br,mid,k): low = mid
        else: high = mid
    if f(ar,br,high,k): print(high)
    elif f(ar,br,low,k): print(low)
    else: print(0)
