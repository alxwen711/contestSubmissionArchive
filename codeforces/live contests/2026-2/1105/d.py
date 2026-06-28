import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ternary search?
this does not appear to be just hand the gift to highest remaining
or if it is, there is a more complex formula

not ternary search, might not be greedy at all
"""

def f(n,d,ar,order,x):
    h = [0]*n
    for i in range(x):
        h[order[i][1]] = 1
    prefix = [0]
    for j in h:
        prefix.append(prefix[-1]+j)
    ans = 0
    # compute the summation totals
    for k in range(n):
        # compute all to right
        hg = 0
        if k+d >= n:
            hg += prefix[n]-prefix[k+1]+prefix[k+d-n+1]
        else:
            hg += prefix[k+d+1]-prefix[k+1]
        # compute all to left
        if k-d < 0:
            hg += prefix[k]+prefix[n]-prefix[n-d+k]
        else:
            hg += prefix[k]-prefix[k-d]
        if h[k] == 1: ans += ar[k]*(2*d-hg)
        else: ans -= ar[k]*hg
    return ans

for _ in range(readint()):
    n,d = readints()
    ar = readar()
    order = list()
    for i in range(n):
        order.append((ar[i],i))
    order.sort()
    order.reverse()
    #print(order)
    low = 0
    high = n
    while high - low > 10:
        diff = high-low
        mid1 = low+diff//3
        mid2 = low+(diff//3*2)
        a = f(n,d,ar,order,mid1)
        b = f(n,d,ar,order,mid2)
        if b >= a: low = mid1
        if a >= b: high = mid2
    ans = 0
    for snth in range(low,high+1):
        print(snth,f(n,d,ar,order,snth))
        ans = max(ans,f(n,d,ar,order,snth))
    print(ans)
        
