import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
Alice optimal array is
0 1 1 2 2 2 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5...
just has to be n of a value, then n-1, n-2, n-3

0 0 1 1 2 can result in 3
0 0 1 1 2 2 3 3 4 5 5 6 6
"""
def f(h,x):
    ar = list()
    for i in range(x):
        ar.append(h[i])
    ar.sort()
    for j in range(x):
        if ar[j] <= j: return False
    return True

for _ in range(readint()):
    n = readint()
    ar = readar()
    h = [0]*n
    for i in ar:
        h[i] += 1
    ans = 0
    flag = True
    for j in range(n):
        if h[j] == 0: break
        elif h[j] == 1:
            if flag: flag = False
            else: break
        ans += 1
    print(ans)
    """
    low = 0
    high = n
    while high-low > 1:
        mid = (low+high)//2
        if f(h,mid): low = mid
        else: high = mid
    if f(h,high): print(high)
    else: print(low)
    """
