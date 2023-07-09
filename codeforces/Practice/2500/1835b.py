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
why in the world is -2 -1 0 +1 +2 always containing optimal
"""
"""
def binrank(n,ar,x,tie):
    l = 0
    h = n-1
    if tie:
        while h-l > 1:
            mid = (l+h)//2
            if ar[mid] < x: l = mid
            elif ar[mid] > x: h = mid
            else: l = mid
        if ar[h] <= x: return h+1
        elif ar[l] <= x: return l+1
        return l
    else:
        while h-l > 1:
            mid = (l+h)//2
            if ar[mid] < x: l = mid
            elif ar[mid] > x: h = mid
            else: h = mid 
        if ar[h] < x: return h+1
        elif ar[l] < x: return l+1
        return l
"""
def f(n,m,k,ar,x,bl,bh):
    #bl = binrank(n,ar,x,False) #lowest index
    #bh = binrank(n,ar,x,True) #highest index
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
    return maxc-minc+1


    
def solve(n,m,k,ar):
    if k > n: return m+1,0
    ans = 0
    lr = 0
    hr = ar.count(0) #O(n) should be fine here
    best = f(n,m,k,ar,0,lr,hr)
    x = max(ar[0]-2,0)
    for i in range(n):
        x = max(x,ar[i]-2)
        while x <= m:
            # c = f(n,m,k,ar,x)
            while lr != n:
                if x > ar[lr]: lr += 1
                else: break
            while hr != n:
                if x >= ar[hr]: hr += 1
                else: break
            c = f(n,m,k,ar,x,lr,hr)
            if c > best:
                best = c
                ans = x
            if ar[i]+2 == x: break
            x += 1            
    return best,ans
    

n,m,k = readints()
ar = readar()
ar.sort()
a,b = solve(n,m,k,ar)
if a >= 0: print(a,b)
else: print(0,0)
