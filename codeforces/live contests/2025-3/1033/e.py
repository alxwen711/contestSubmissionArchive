import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
binary search: the question

number of lanes moved does not matter
just move highest to lowest until no added benefit???
bsearch over 0 to imbalance for x, where:
x is as large as possible
xth furthest car would gain benefit by moving into xth closest position
then move that many cars
"""

def f(n,k,ar,x,s): # is moving the xth furthest car to xth closest empty viable

    # find the xth furthest car
    low = 1
    high = ar[-1]
    while high-low > 1:
        mid = (low+high)//2
        r = s
        for i in ar:
            r -= min(i,mid)
        if r >= x: low = mid
        else: high = mid
    pos = low
    r = s
    for i in ar:
        r -= min(i,low)
    if r >= x: pos = high

    # det if xth closest spot actually saves time
    req = pos-k-1
    snth = 0
    for u in ar:
        if u >= req: break
        snth += req-u
    if snth >= x: return pos
    return -1

def f2(n,k,ar,mid,x):
    req = x
    for i in ar:
        if i >= mid: break
        req -= (mid-i)
        if req <= 0: return True
    return False

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    ar.sort()
    s = sum(ar)
    linelimit = (s+n-1)//n
    imbalance = 0 # maximum number of cars to move
    for i in range(n):
        imbalance += max(0,ar[i]-((s+i)//n))
    low = 0
    high = imbalance
    while high-low > 1:
        mid = (low+high)//2
        if f(n,k,ar,mid,s) != -1: low = mid
        else: high = mid
    x = low
    if f(n,k,ar,high,s) != -1: x = high

    # move x cars
    pos = f(n,k,ar,x,s) # xth furthest car is somewhere here
    req = x
    for i in range(n):
        diff = ar[i]-pos
        if diff > 0:
            req -= diff
            ar[i] = pos
    for j in range(req):
        ar[-j-1] -= 1
    #ar.sort()
    #print(ar)
    ar.sort()
    low = 1
    high = pos

    while high-low > 1:
        mid = (low+high)//2
        if f2(n,k,ar,mid,x): high = mid
        else: low = mid
    ans = k*x
    # use low limit, then increment to high
    for i in range(n):
        diff = max(0,low-ar[i])
        if diff != 0:
            x -= diff
            ar[i] += diff
    for snth in range(x):
        ar[snth] += 1

    # get the answer
    
    for u in ar:
        ans += (u*u+u)//2
    print(ans)
    #print(ar)
    
