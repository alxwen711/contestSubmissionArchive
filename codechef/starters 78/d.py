import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def f(dr,p,save,x,mid):
    req = dr[mid]
    if mid > p: req -= save
    return x >= req

def bsearch(dr,p,x):
    save = dr[p+1]-dr[p]
    low = 0
    high = len(dr)-1
    while high-low > 1:
        mid = (high+low)//2
        if f(dr,p,save,x,mid): low = mid
        else: high = mid
    if f(dr,p,save,x,high): return high
    return low

for i in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    cr = list()
    for j in range(n):
        cr.append([ar[j]+br[j],ar[j]])
    cr.sort()
    dr = list()
    dr.append(0)
    rsum = 0
    for l in range(n):
        rsum += cr[l][0]
        dr.append(rsum)
    done = False
    ans = 0
    #print(cr)
    #print(dr)
    for p in range(n):
        if cr[p][1] <= k: #completable task
            lp = bsearch(dr,p,k-cr[p][1])
            #print(p,lp)
            if p >= lp: lp += 1
            ans = max(ans,lp)
    print(ans)
        
