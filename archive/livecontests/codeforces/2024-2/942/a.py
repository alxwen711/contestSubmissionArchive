import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
figure out the maximum cap set possible
"""

def f(ar,k,x):
    s = k
    for i in ar:
        if i < x: s -= (x-i)
        if s < 0: return False
    return True

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    low = 1
    high = 10**13
    while high-low > 1:
        mid = (low+high)//2
        if f(ar,k,mid): low = mid
        else: high = mid
    x = high
    if not f(ar,k,high): x = low
    for i in range(n):
        if ar[i] <= x:
            k -= (x-ar[i])
            ar[i] = x
        else: ar[i] = x+1
    ar.sort()
    for j in range(k):
        ar[j] += 1
    print(sum(ar)-n+1)
