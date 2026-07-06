import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def bsearch(a,br,inc,v):
    low = inc
    high = len(br)-1
    while high-low > 1:
        mid = (low+high)//2
        if br[mid]-v <= a: low = mid
        else: high = mid
    if br[high]-v <= a: return high+1-inc
    elif br[low]-v <= a: return low+1-inc
    return low-inc

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    #cr = [0]*n
    dr = [0]*n
    #x = 0
    y = 0
    for j in range(n):
        #x += br[-1-j]
        y += br[j]
        #cr[-j-1] = x
        dr[j] = y
    #print(dr)
    #print(cr)
    ans = [0]*n
    sr = [0]*n
    er = [0]*(n+2)
    v = 0
    for k in range(n):
        if k != 0: v = dr[k-1]
        g = ar[k]
        f = bsearch(g,dr,k,v)
        if f != 0:
            sr[k] += 1
            er[k+f] += 1
        if k+f != 0: g += (v-dr[k+f-1])
        if k+f < n:
            if g < br[k+f]: ans[k+f] += g
            else: ans += br[k+f]
    inc = 0
    for l in range(n):
        inc += sr[l]-er[l]
        ans[l] += inc*br[l]
        #print(inc,end=" ")
    #print()
    print(*ans)
