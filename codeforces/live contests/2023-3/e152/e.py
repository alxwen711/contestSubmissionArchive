import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
subarray must be minimum length 2
consider each indiv val as maximum,
num of subarrays with that max is number of
vals can traverse back until running into higher
barray to track if EVERYTHING to a point is lower
O(n log n log n)
"""

def initbar(n):
    ar = list()
    while n != 0:
        tmp = [-1]*n
        ar.append(tmp)
        n //= 2
    return ar

def update(ar,x,v):
    ar[0][x] = v
    x //= 2
    for i in range(1,len(ar)):
        if x >= len(ar[i]): break
        ar[i][x] = min(ar[i-1][x*2],ar[i-1][x*2+1])
        x //= 2

def q(a,b,ar): #check min from index a to b
    aa = a
    bb = b
    ans = 8968963394
    level = 0
    while a <= b:
        if a % 2 == 1:
            ans = min(ans,ar[level][a])
            a += 1
        if b % 2 == 0:
            ans = min(ans,ar[level][b])
            b -= 1
        a //= 2
        b //= 2
        level += 1
    #print(aa,bb,ans)
    return ans

n = readint()
ar = readar()

br = initbar(n)
h = [0]*n
for i in range(n):
    h[ar[i]-1] = i

hr = list()
xx = 7598234758942375
for snth in h:
    xx = min(snth,xx)
    hr.append(xx)

ans = 0
value = -1
for x in h: #update pos x, det len of segment comprising all 1's
    value += 1
    update(br,x,value)
    lv = 1
    rv = 1
    #compute lv
    low = 0
    high = x
    #print(br)
    while high-low > 1:
        mid = (low+high)//2
        if q(x-mid,x,br) != -1: low = mid
        else: high = mid
    if q(x-high,x,br) != -1: lv += high
    else: lv += low

    """
    compute "rv", ie. look at later right elements
    see if maximum is still possible?
    also problem is that each value to right may change the new left boundary
    1 4 7 8 6 5 4 3 2
    with max 8, can extend to all right vals, but
    amount of left extension will then be affected
    
    low = 0
    high = n-x-1
    while high-low > 1:
        mid = (low+high)//2
        if q(x+mid,br)-q(x-1,br) == mid+1: low = mid
        else: high = mid
    if q(x+high,br)-q(x-1,br) == high+1: rv += high
    else: rv += low
    """
    ans += (lv-1)
    
print(ans)
