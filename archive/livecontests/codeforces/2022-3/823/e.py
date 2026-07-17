import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from random import randint

"""
entire solution only runs in O(n^1.71) at best, need at least O(n log n)
By master theorem, even if assuming best case, T(n) = 2T(2n/3) + T(n/3) + O(1)
"""
def mincreate_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (min(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def minquery(l: int, h: int, ar: list[list]):
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l]
    else: return min(ar[ex][l],ar[ex][h-two+1])

def maxcreate_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (max(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def maxquery(l: int, h: int, ar: list[list]):
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l]
    else: return max(ar[ex][l],ar[ex][h-two+1])

def freq_dict(ar, pos = False) -> dict:
    d = {}
    if ar == None: return d
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None:
            if pos: d[x] = list()
            else: d[x] = 0
        if pos: d[x].append(i)
        else: d[x] += 1
    return d

def filt(ar,x,y):
    low,high = 0,len(ar)-1
    if low == high: return ar
    lowi,highi = -1,-1
    #search for low
    while high - low > 1:
        mid = (low+high)//2 
        if ar[mid] >= x: high = mid
        else: low = mid
    if ar[low] >= x: lowi = low
    else: lowi = high


    #search for high
    low,high = 0,len(ar)-1
    
    while high - low > 1:
        mid = (low+high)//2 
        if ar[mid] <= y: low = mid
        else: high = mid

    #diff is small enough
    if ar[high] <= y: highi = high+1
    else: highi = low+1

    return ar[lowi:highi]

def solve(ar,mins,maxs,a,b,d):
    if b-a < 1: return b-a+1
    if b-a == 1:
        if max(ar[a],ar[b]) % min(ar[a],ar[b]) == 0: return 3
        else: return 2
    low,high = minquery(a,b,mins),maxquery(a,b,maxs)
    lh = filt(d[low],a,b)
    hh = filt(d[high],a,b)
    lt,ht = (((b-a)//3)+a),((2*(b-a)//3)+a)
    pbest = 987369873345
    li,hi = -1,-1
    for k in range(10):
        if k == 0: x,y = lh[0],hh[0]
        elif k == 1: x,y = lh[0],hh[-1]
        elif k == 2: x,y = lh[-1],hh[0]
        elif k == 3: x,y = lh[-1],hh[-1]
        else: x,y = lh[randint(0,len(lh)-1)],hh[randint(0,len(hh)-1)]        
        if x > y: #swap
            tmp = y
            y = x
            x = tmp
        metric = (abs(x-lt)+abs(y-ht)) 
        if metric < pbest:
            pbest = metric
            li,hi = x,y
    #print(d[low],d[high],low,high,li,hi)
    if high % low == 0: #determine how many to add
        ans = (li-a+1)*(b-hi+1)
        #print((a,hi-1),(li+1,b),(li+1,hi-1))
        return solve(ar,mins,maxs,a,hi-1,d)+solve(ar,mins,maxs,li+1,b,d)-solve(ar,mins,maxs,li+1,hi-1,d)+ans
    else:
        return solve(ar,mins,maxs,a,hi-1,d)+solve(ar,mins,maxs,li+1,b,d)-solve(ar,mins,maxs,li+1,hi-1,d)

for i in range(readint()):
    n = readint()
    ar = readar()
    mins = mincreate_sparse(ar)
    maxs = maxcreate_sparse(ar)
    d = freq_dict(ar,True)
    print(solve(ar,mins,maxs,0,n-1,d))
