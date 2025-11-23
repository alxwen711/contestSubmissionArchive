import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
probably not binary search?
erase lowest values?
24667889 goes to 2? (apparently no)

answer is at most minval

anything up to //4 is possible, original value, or if divisible by 3, //3

for each value, count numbers at least 4x, count x, count 3x
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    ar.sort()
    h = [0]*(n+1)
    for i in ar:
        h[i] += 1
    ans = 1
    for j in range(2,ar[-1]+1):
        v = h[j]
        if j*2 <= n: v += h[j*2]
        if j*3 <= n: v += h[j*3]
        # binary search for values at least 4j
        low = 0
        high = n-1
        target = 4*j
        while high-low > 1:
            mid = (low+high)//2
            if ar[mid] >= target: high = mid
            else: low = mid
        if ar[low] >= target: v += (n-low)
        elif ar[high] >= target: v += (n-high)
        if v >= (n-k):
            ans = j
    print(ans)
