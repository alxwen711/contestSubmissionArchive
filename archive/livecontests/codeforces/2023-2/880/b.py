import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# order does not matter since you always lose tb
"""
find kth closest for each point to get win range
this just uses sliding window? how to adjust with large m?
det l/h pts for each win range
when passing l, +1, pass h -> -1
highest score and lowest index is ans
only have to consider spots at or adjacent to another point? +0?
what "rank" would your ticket be, if marker in range of pts
then auto win, else find furthest one out on each end, det when
lose point occurs

by circumstance out of time
if this is just ternary search with a mountain i swear to god
"""

def binrank(n,ar,x,tie):
    l = 0
    h = n-1
    while h-l > 1:
        mid = (l+h)//2
        if ar[mid] < x: l = mid
        elif ar[mid] > x: h = mid
        elif tie: l = mid
        else: h = mid
    if tie:
        if ar[h] <= x: return h+1
        elif ar[l] <= x: return l+1
        return l
    else:
        if ar[h] < x: return h+1
        elif ar[l] < x: return l+1
        return l

def f(n,m,k,ar,x):
    bl = binrank(n,ar,x,False) #lowest index
    bh = binrank(n,ar,x,True) #highest index
    #determine min cap
    minc = 0
    if bh >= k:
        lim = ar[bh-k]
        dist = x-lim
        req = (dist//2)+1
        minc = lim+req
    #determine max cap
    maxc = m
    ll = bl+k-1
    if ll < n:
        lim = ar[ll]
        dist = lim-x
        req = (dist//2)
        maxc = x+req
        if dist % 2 == 0: maxc -= 1
    #print(x,minc,maxc)
    return max(0,maxc-minc+1)


    
def solve(n,m,k,ar):
    if k > n: return m+1,0
    ans = 0
    best = f(n,m,k,ar,0)
    for i in ar:
        x = i
        if x != 0:
            c = f(n,m,k,ar,x-1)
            if c > best:
                best = c
                ans = x-1
            elif c == best and (x-1) < ans: ans = x-1
        if x != m:
            c = f(n,m,k,ar,x+1)
            if c > best:
                best = c
                ans = x+1
            elif c == best and (x+1) < ans: ans = x+1
        c = f(n,m,k,ar,x)
        if c > best:
            best = c
            ans = x
        elif c == best and x < ans: ans = x
    return best,ans
    

n,m,k = readints()
ar = readar()
ar.sort()
a,b = solve(n,m,k,ar)
if b != 0 and b < ar[0]: #lower index is possible
    l = 0
    h = b
    while h-l > 1:
        mid = (l+h)//2
        if f(n,m,k,ar,mid) == a: h = mid
        else: l = mid
    b = l
    if f(n,m,k,ar,b) != a: b += 1 #h
print(a,b)
