import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
#O(n^3) will work, maybe O(n^4) or even O(n^5)
#only need to check up to about 50 mil*50 = 2.5 billion?
"""
check each pair for what values are possible
time limit is passing easily??
0,1,3,6,10...
"""


def ff(a,b):
    ans = list()
    diff = b-a
    
    if diff % 2 == 1: #odd case
        for u in range(1,round(diff**0.5)+4,2):
            if diff % u == 0:
                mid = diff//u
                mid -= u
                mid += 1
                e = (mid//2)**2
                if e < a or mid < 0: break
                else: ans.append(e-a)
    else: # %2 but not %4 is impossible?
        for u in range(2,round(diff**0.5)+4,2):
            if diff % u == 0:
                mid = diff//u
                if mid % 2 == 0:
                    mid = mid-u+1
                    e = (mid//2)**2
                    if e < a or mid < 0: break
                    else: ans.append(e-a)
    return ans


def square(x):
    low = 0
    high = 51000000
    while high-low > 1:
        mid = (low+high)//2
        y = mid*mid
        if y == x: return True
        elif y > x: high = mid
        else: low = mid
    return (low*low == x) or (high*high == x)

#squares = {}
#for j in range(50000001):
#    squares[j*j] = 1
for i in range(readint()):
    n = readint()
    ar = readar()
    v = {}
    for a in range(n):
        for b in range(a+1,n):
            c = ff(ar[a],ar[b])
            for k in range(len(c)):
                if v.get(c[k]) == None: v[c[k]] = 0
                v[c[k]] += 1
    d = list(v.keys())
    #print(a,b,d)
    best = 0
    for m in range(len(d)):
        """
        x = 0
        y = d[m]
        for p in range(n):
            #if squares.get(ar[p]+y) == 1: x += 1
            if square(ar[p]+y): x += 1
        best = max(x,best)
        """
        best = max(best,v[d[m]])
    ans = 0
    for kk in range(51):
        if (kk*kk+kk)//2 == best:
            ans = kk+1
            break
    print(ans)
