import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
given n elements,
C(n-1,2),C(n-2,2),C(n-3,2)...,C(2,2)

"""

def ray(n):
    s = 0
    ar = list()
    for i in range(n-2):
        s += ((n-i-1)*(n-i-2))//2
        ar.append(s)
    return ar


def f(k,br):
    low = 0
    high = len(br)-1
    while high-low > 1:
        mid = (low+high)//2
        if br[mid] < k: low = mid
        else: high = mid
    if br[low] >= k: return low
    return high

for i in range(readint()):
    n,q = readints()
    ar = readar()
    ar.sort()
    br = ray(n)
    #print(br)
    for j in range(q):
        k = readint()
        print(ar[f(k,br)])
