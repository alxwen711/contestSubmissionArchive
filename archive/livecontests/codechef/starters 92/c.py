import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
greedily choose most frequent candy first
or bin search answer by assigning most even distribution possible
and checking if each one can be used?
"""

def f(n,k,ar,x,s):
    if x == 0: return True
    req = k*x
    rem = n
    high = 0
    for i in range(n):
        if ar[i]*rem >= req:
            left = req//rem
            if req % rem != 0: left += 1
            high = max(high,left)
            break
        else:
            rem -= 1
            req -= ar[i]
            high = ar[i]
    used = x*k
    if high*k > used: return False
    return True
        

def solve(n,k,ar):
    low = 0
    s = sum(ar)
    high = s//k
    ar.sort()
    while high-low > 1:
        mid = (low+high)//2
        if f(n,k,ar,mid,s): low = mid
        else: high = mid
    if f(n,k,ar,high,s): return high
    return low


for i in range(readint()):
    n,k = readints()
    ar = readar()
    print(solve(n,k,ar))
