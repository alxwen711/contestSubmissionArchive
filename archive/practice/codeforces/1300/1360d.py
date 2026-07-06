import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = list()
    x = 1
    while x*x <= n:
        if n % x == 0:
            ar.append(x)
            ar.append(n//x)
        x += 1
    ar.sort()
    low = 0
    high = len(ar)-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] > k: high = mid
        else: low = mid
    if ar[high] <= k: print(n//ar[high])
    else: print(n//ar[low])
    
        
