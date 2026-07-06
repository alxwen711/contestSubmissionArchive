import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = readar()
br = readar()

rt = [0]
for i in range(n):
    rt.append(rt[-1]+br[i])
#print(rt)
for _ in range(readint()):
    l,r = readints()
    li,ri = -1,-1
    # left index
    low = 0
    high = n-1
    while high - low > 1:
        #print(low,high)
        mid = (low+high)//2
        if ar[mid] >= l: high = mid
        else: low = mid
    #print(low,high,l,r)
    if ar[low] >= l: li = low
    elif ar[high] >= l: li = high
    else: li = high+1

    # right index
    low = 0
    high = n-1
    while high - low > 1:
        #print(low,high)
        mid = (low+high)//2
        if ar[mid] <= r: low = mid
        else: high = mid
    #print(low,high,l,r)
    if ar[high] <= r: ri = high
    elif ar[low] <= r: ri = low
    else: ri = low-1
    if low > high: print(0)
    else: print(rt[ri+1]-rt[li])

    
