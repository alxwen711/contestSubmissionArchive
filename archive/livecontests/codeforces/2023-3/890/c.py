import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
sum of n is at most 1000
is there a way to determine if a maximum is possible? if so bin search

"""

def inc(n,k,ar,x,i):
    rv = x
    t = 0
    while i != n-1:
        iv = max(0,rv-ar[i])
        if iv == 0: # end calcs
            if t > k: return False
            return True
        t += iv
        rv -= 1
        i += 1
    # last run for last val
    if ar[-1] >= rv and k >= t: return True
    return False

def f(n,k,ar,x):
    for i in range(n-1):
        if inc(n,k,ar,x,i): return True
    return False

def b(n,k,ar):
    low = max(ar)+1
    high = low-1+k
    while high-low > 1:
        mid = (low+high)//2
        if f(n,k,ar,mid): low = mid
        else: high = mid
    if f(n,k,ar,high): return high
    elif f(n,k,ar,low): return low
    return low-1

for i in range(readint()):
    n,k = readints()
    ar = readar()
    print(b(n,k,ar))
